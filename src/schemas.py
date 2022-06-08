"""contains Pandera schemas for dataframes"""

import pandera as pa

RD_NO_PAT = r"[A-Z]{1,2}\d{6}"

status_schema = pa.DataFrameSchema(
    columns={
        "rd": pa.Column(str, checks=[pa.Check.str_matches(RD_NO_PAT)]),
        "homicide_no": pa.Column(str),
        "injury_date": pa.Column("datetime64[ns]"),
        "death_date": pa.Column("datetime64[ns]"),
        "compstat_date": pa.Column("datetime64[ns]"),
        "address_block_level": pa.Column(str),
        "homicide_location_descr": pa.Column(str),
        "victim_sex": pa.Column(
            str,
            checks=[pa.Check.isin(["male", "female", "unknown/other"])],
            nullable=True,
        ),
        "cleared_i": pa.Column(bool),
        "cleared_exceptionally_by": pa.Column(
            str,
            checks=[pa.Check.isin(["DEATH OF OFFENDER", "BAR TO PROSECUTE"])],
            nullable=True,
        ),
        "date_cleared": pa.Column("datetime64[ns]", nullable=True),
    }
)

victims_schema = pa.DataFrameSchema(
    columns={
        "case_number": pa.Column(str, checks=[pa.Check.str_matches(RD_NO_PAT)]),
        "victim_race": pa.Column(
            str,
            checks=[
                pa.Check.isin(
                    [
                        "black",
                        "white",
                        "hispanic",
                        "api",
                        "indian",
                        "unknown",
                    ]
                )
            ],
        ),
    }
)
