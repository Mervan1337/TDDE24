# Write your code for lab 8d here.

from test_driver import store_test_case, run_free_spans_tests


# Create additional test cases, and add to them to create_tests_for_free_span().

def create_tests_for_free_span() -> dict:
    """Create and return a number of test cases for the free_spans function"""
    test_cases = dict()

    """
    Test Case 1
    
    Testar generell funktionallitet.
    
    """

    store_test_case(
        test_cases,
        1,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=["09:00-13:00", "18:00-21:00"],
    )  # Expected free time

    # -------- YOUR TEST CASES GO HERE -----------------------
    # For each case, add a brief description of what you want to test.

    """
    Test Case 2
    
    Testar ifall inga dagar ligger bokade.
    Samt om den kollar hela dagen.
    
    """
    store_test_case(
        test_cases,
        2,
        start_str="00:00",  # Search interval starts
        end_str="23:59",  # Search interval ends
        booking_data=[],  # This day's appointments
        exp_result=["00:00-23:59"],
    )  # Expected free time

    """
    Test Case 3

    Testar två appointments efter varandra så att den inte "hittar" en free time mellan dessa.

    """
    store_test_case(
        test_cases,
        3,
        start_str="09:00",  # Search interval starts
        end_str="16:00",  # Search interval ends
        booking_data=["10:00-13:00", "13:00-20:00"],  # This day's appointments
        exp_result=["09:00-10:00"],
    )  # Expected free time

    """
    Test Case 4
    
    Fall då start och end ligger innanför en bokning, då skall den returnera en tom TimeSpanSeq.

    """
    store_test_case(
        test_cases,
        4,
        start_str="12:00",  # Search interval starts
        end_str="16:00",  # Search interval ends
        booking_data=["00:00-17:00"],  # This day's appointments
        exp_result=[],
    )  # Expected free time

    """
               Test Case 5

               Testar fall om dagen är fylld (3 appointments driekt efter varandra)

        """
    store_test_case(
        test_cases,
        5,
        start_str="00:00",  # Search interval starts
        end_str="23:59",  # Search interval ends
        booking_data=["00:00-10:00","10:00-15:00","15:00-23:59"],  # This day's appointments
        exp_result=[],
    )  # Expected free time


    print("Test cases generated.")

    return test_cases


if __name__ == '__main__':
    # Actually run the tests, using the test driver functions
    tests = create_tests_for_free_span()
    run_free_spans_tests(tests)
