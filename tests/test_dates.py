import project1

from project1 import redactor

import pytest




d = """Tom Cruise is an American actor known for his roles in iconic films throughout the August 2 1980, as well as his high profile marriages to actresses Nicole Kidman and Katie Holmes.
After developing an interest in acting during high school, he rocketed to fame with his star turns in Risky Business and Top Gun. Cruise later earned acclaim for his work in the hit film Jerry Maguire and the Mission: Impossible franchise.
Early Life Thomas Cruise Mapother IV, better known as Tom Cruise, was born on July 3, 1962, in Syracuse, New York, to Mary and Thomas Mapother. Cruise's mother was an amateur actress and schoolteacher, and his father was an electrical engineer. 
His family moved around a great deal when Cruise was a child to accommodate his father's career."""


def test_date():
    (t, da, c) = redactor.redact_dates (d)
    assert c ==4
    assert ['August 2 1980', 'July 3, 1962', 'August', 'July'] == da
   
     
