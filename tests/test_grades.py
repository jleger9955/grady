from grades import get_grades, get_averages, rank_scores


def test_get_grades():
    grades = get_grades('grades.txt')
    d = {'bob': [78.0, 88.0, 90.0], 'sara': [98.0], 'sue': [72.0, 95.0]}
    assert grades == d


def test_get_averages():
    grades = get_grades('grades.txt')
    avgs = get_averages(grades)
    assert avgs == [('bob', 85.33333333333333), ('sara', 98.0), ('sue', 83.5)]


def test_rank_scores():
    grades = get_grades('grades.txt')
    avgs = get_averages(grades)
    rank = rank_scores(avgs)
    assert rank == [('sara', 98.0), ('bob', 85.33333333333333), ('sue', 83.5)]
