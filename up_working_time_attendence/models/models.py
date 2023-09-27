# -*- coding: utf-8 -*-

from odoo import models, fields, api ,_
from odoo.exceptions import ValidationError, UserError
from itertools import chain
from odoo.tools.float_utils import float_round


def _boundaries(intervals, opening, closing):
    """ Iterate on the boundaries of intervals. """
    for start, stop, recs in intervals:
        if start < stop:
            yield (start, opening, recs)
            yield (stop, closing, recs)





class Intervals(object):
    """ Collection of ordered disjoint intervals with some associated records.
        Each interval is a triple ``(start, stop, records)``, where ``records``
        is a recordset.
    """
    def __init__(self, intervals=()):
        self._items = []
        if intervals:
            # normalize the representation of intervals
            append = self._items.append
            starts = []
            recses = []
            for value, flag, recs in sorted(_boundaries(intervals, 'start', 'stop')):
                if flag == 'start':
                    starts.append(value)
                    recses.append(recs)
                else:
                    start = starts.pop()
                    if not starts:
                        append((start, value, recses[0].union(*recses)))
                        recses.clear()

    def __bool__(self):
        return bool(self._items)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __reversed__(self):
        return reversed(self._items)

    def __or__(self, other):
        """ Return the union of two sets of intervals. """
        return Intervals(chain(self._items, other._items))

    def __and__(self, other):
        """ Return the intersection of two sets of intervals. """
        return self._merge(other, False)

    def __sub__(self, other):
        """ Return the difference of two sets of intervals. """
        return self._merge(other, True)

    def _merge(self, other, difference):
        """ Return the difference or intersection of two sets of intervals. """
        result = Intervals()
        append = result._items.append

        # using 'self' and 'other' below forces normalization
        bounds1 = _boundaries(self, 'start', 'stop')
        bounds2 = _boundaries(other, 'switch', 'switch')

        start = None                    # set by start/stop
        recs1 = None                    # set by start
        enabled = difference            # changed by switch
        for value, flag, recs in sorted(chain(bounds1, bounds2)):
            if flag == 'start':
                start = value
                recs1 = recs
            elif flag == 'stop':
                if enabled and start < value:
                    append((start, value, recs1))
                start = None
            else:
                if not enabled and start is not None:
                    start = value
                if enabled and start is not None and start < value:
                    append((start, value, recs1))
                enabled = not enabled

        return result


# ___________________________-



class ResourceCalenderInherit(models.Model):
    _inherit = 'resource.calendar'

    @api.onchange('attendance_ids', 'two_weeks_calendar')
    def _onchange_hours_per_day(self):
        attendances = self._get_global_attendances()
        # print('lenth ' , len(attendances))
        # print(self.hours_per_week,"htotal ")
        self.hours_per_day = self.hours_per_week /len(attendances)



    def _compute_hours_per_week(self):
        sum_hours=0
        for calendar in self:
            for attendance in  calendar.attendance_ids:
                if not attendance.work_entry_type_id.is_leave:
                    if attendance.cross_day:
                        sum_hours += (24 - attendance.hour_from ) + attendance.hour_to
                    else:
                        sum_hours += attendance.hour_to - attendance.hour_from

        calendar.hours_per_week = sum_hours / 2 if calendar.two_weeks_calendar else sum_hours




    def _compute_hours_per_day(self, attendances):
        if not attendances:
            return 0

        hour_count = 0.0
        for attendance in attendances:
            if attendance.cross_day:
                hour_count =( 24 - attendance.hour_from) + attendance.hour_to

            else:
                hour_count += attendance.hour_to - attendance.hour_from

        if self.two_weeks_calendar:
            number_of_days = len(set(attendances.filtered(lambda cal: cal.week_type == '1').mapped('dayofweek')))
            number_of_days += len(set(attendances.filtered(lambda cal: cal.week_type == '0').mapped('dayofweek')))
        else:
            number_of_days = len(set(attendances.mapped('dayofweek')))

        return float_round(hour_count / float(number_of_days), precision_digits=2)
        return  10

        # return super(ResourceCalenderInherit,self)._compute_hours_per_day(attendances)

    # def _onchange_hours_per_day(self):
    #     attendances = self._get_global_attendances()
    #     self.hours_per_day = self._compute_hours_per_day(attendances)
    #


    def _check_overlap(self, attendance_ids):
        """ attendance_ids correspond to attendance of a week,
            will check for each day of week that there are no superimpose. """
        midnight_shift = False
        result = []
        for attendance in attendance_ids.filtered(lambda att: not att.date_from and not att.date_to):
            if attendance.cross_day:
                midnight_shift =True
            # 0.000001 is added to each start hour to avoid to detect two contiguous intervals as superimposing.
            # Indeed Intervals function will join 2 intervals with the start and stop hour corresponding.
            result.append((int(attendance.dayofweek) * 24 + attendance.hour_from + 0.000001, int(attendance.dayofweek) * 24 + attendance.hour_to, attendance))


        if not midnight_shift and  len(Intervals(result)) != len(result):
            raise ValidationError(_("Attendances can't overlap."))












class UpworkingAtimeAttendence(models.Model):
    _inherit='resource.calendar.attendance'
    cross_day = fields.Boolean(string='Extends overnight')

    # override
    @api.onchange('hour_from', 'hour_to','cross_day')
    def _onchange_hours(self):
        # avoid negative or after midnight
        self.hour_from = min(self.hour_from, 23.99)
        self.hour_from = max(self.hour_from, 0.0)
        self.hour_to = min(self.hour_to, 24)
        self.hour_to = max(self.hour_to, 0.0)

        if self.cross_day ==True:
            return
        self.hour_to = max(self.hour_to, self.hour_from)



