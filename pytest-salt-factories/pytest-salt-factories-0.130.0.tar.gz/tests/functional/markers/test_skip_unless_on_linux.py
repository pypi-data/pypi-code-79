"""
    tests.functional.markers.test_skip_unless_on_linux
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Test the ``@pytest.mark.skip_unless_on_linux`` marker
"""
from unittest import mock


def test_skipped(pytester):
    pytester.makepyfile(
        """
        import pytest

        @pytest.mark.skip_unless_on_linux
        def test_one():
            assert True
        """
    )
    return_value = False
    with mock.patch("saltfactories.utils.platform.is_linux", return_value=return_value):
        res = pytester.runpytest_inprocess()
        res.assert_outcomes(skipped=1)
    res.stdout.no_fnmatch_line("*PytestUnknownMarkWarning*")


def test_not_skipped(pytester):
    pytester.makepyfile(
        """
        import pytest

        @pytest.mark.skip_unless_on_linux
        def test_one():
            assert True
        """
    )
    return_value = True
    with mock.patch("saltfactories.utils.platform.is_linux", return_value=return_value):
        res = pytester.runpytest_inprocess()
        res.assert_outcomes(passed=1)
    res.stdout.no_fnmatch_line("*PytestUnknownMarkWarning*")


def test_skip_reason(pytester):
    pytester.makepyfile(
        """
        import pytest

        @pytest.mark.skip_unless_on_linux(reason='Because!')
        def test_one():
            assert True
        """
    )
    return_value = False
    with mock.patch("saltfactories.utils.platform.is_linux", return_value=return_value):
        res = pytester.runpytest_inprocess("-ra", "-s", "-vv")
        res.assert_outcomes(skipped=1)
    res.stdout.fnmatch_lines(["SKIPPED * test_skip_reason.py:*: Because!"])
