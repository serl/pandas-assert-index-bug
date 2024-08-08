from pandas import DataFrame
from pandas.testing import assert_frame_equal


def main():
    df_1 = DataFrame(
        {
            "name": ["John", "Anna", "Peter", "Linda"],
            "surname": ["Smith", "Jones", "Brown", "Wilson"],
            "age": [23, 36, 33, 26],
            "city": ["New York", "Paris", "Berlin", "London"],
        }
    ).set_index(["name", "surname"])

    df_cities = df_1.assign(city=["A", "B", "C", "D"])
    try:
        assert_frame_equal(df_1, df_cities, obj="df_cities")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        # AssertionError: df_cities.iloc[:, 1] (column name="city") are different <== the obj parameter is used

    print("===")

    df_surnames = (
        df_1.reset_index()
        .assign(surname=["A", "B", "C", "D"])
        .set_index(["name", "surname"])
    )
    try:
        assert_frame_equal(df_1, df_surnames, obj="df_surnames")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        # AssertionError: MultiIndex level [1] are different <== the obj parameter is ignored!

    print("===")

    df_2 = DataFrame(
        {
            "name": ["John", "Anna", "Peter", "Linda"],
            "age": [23, 36, 33, 26],
            "city": ["New York", "Paris", "Berlin", "London"],
        }
    ).set_index(["name"])

    df_names = df_2.reset_index().assign(name=["A", "B", "C", "D"]).set_index(["name"])
    try:
        assert_frame_equal(df_2, df_names, obj="df_names")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        # AssertionError: df_names.index are different <== the obj parameter is used


if __name__ == "__main__":
    main()
