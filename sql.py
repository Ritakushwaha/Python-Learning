# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 18:56:19 2021

@author: rikushwa
"""

select concat('Student ',student.id,' has grade:'),
case 
when score>= 80 then 'A'
when score >= 60 and score<80 then 'B'
when score >= 40 and score<60 then 'C'
when score>= 20 and score<40 then 'D'
when score<20 then 'F'
end student_grade
from student;