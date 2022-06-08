"""contains Pandera schemas for dataframes"""

import pandera as pa

RD_NO_PAT = r"[A-Z]{1,2}\d{6}"

status_schema = pa.DataFrameSchema(
    columns={
        "case_no": pa.Column(str, checks=[pa.Check.str_matches(RD_NO_PAT)]),
        "homicide_no": pa.Column(str),
        "injury_date": pa.Column("datetime64[ns]"),
        "death_date": pa.Column("datetime64[ns]"),
        "compstat_date": pa.Column("datetime64[ns]"),
        "address_block_level": pa.Column(str),
        "homicide_location_descr": pa.Column(str),
        "cleared_i": pa.Column(bool),
        "cleared_exceptionally_by": pa.Column(
            str,
            checks=[pa.Check.isin(["DEATH OF OFFENDER", "BAR TO PROSECUTE"])],
            nullable=True,
        ),
        "date_cleared": pa.Column("datetime64[ns]", nullable=True),
        "incident_year": pa.Column(int),
        "clearance_year": pa.Column(
            float, checks=[pa.Check.isin(range(2010, 2023))], nullable=True
        ),
    }
)

victims_schema = pa.DataFrameSchema(
    columns={
        "case_no": pa.Column(str, checks=[pa.Check.str_matches(RD_NO_PAT)]),
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
