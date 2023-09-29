## Variables
{ "accountNumber": "A-A619AE23", "fromDatetime": "2023-09-27T00:00:00.000Z", "toDatetime": "2023-09-28T00:00:00.000Z" }

## headers(token)
{
  "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImlzcyI6Imh0dHBzOi8vYXBpLm9lanAta3Jha2VuLmVuZXJneS92MS9ncmFwaHFsLyJ9.eyJzdWIiOiJrcmFrZW58YWNjb3VudC11c2VyOjI1NDI3NiIsImd0eSI6IkVNQUlMLUFORC1QQVNTV09SRCIsImVtYWlsIjoicGFkLnN1cGVydDAzMTBAZ21haWwuY29tIiwidG9rZW5Vc2UiOiJhY2Nlc3MiLCJpc3MiOiJodHRwczovL2FwaS5vZWpwLWtyYWtlbi5lbmVyZ3kvdjEvZ3JhcGhxbC8iLCJpYXQiOjE2OTU4ODc4ODUsImV4cCI6MTY5NTg5MTQ4NSwib3JpZ0lhdCI6MTY5NTg4Nzg4NX0.Gq5Wz9AXF23OietaRDTozGGqYT5EbQh6TjhZmLsTNZ8"
}

## query
	query halfHourlyReadings(
		$accountNumber: String!
		$fromDatetime: DateTime
		$toDatetime: DateTime
	) {
		account(accountNumber: $accountNumber) {
			properties {
				electricitySupplyPoints {
					agreements {
						validFrom
					}
					halfHourlyReadings(
						fromDatetime: $fromDatetime
						toDatetime: $toDatetime
					) {
						startAt
						value
						costEstimate
						consumptionStep
						consumptionRateBand
					}
				}
			}
		}
	}

## response
{
  "data": {
    "account": {
      "properties": [
        {
          "electricitySupplyPoints": [
            {
              "agreements": [
                {
                  "validFrom": "2023-08-02T15:00:00+00:00"
                }
              ],
              "halfHourlyReadings": [
                {
                  "startAt": "2023-09-27T00:00:00+00:00",
                  "value": "0.05",
                  "costEstimate": "1.64",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T00:30:00+00:00",
                  "value": "0.13",
                  "costEstimate": "4.27",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T01:00:00+00:00",
                  "value": "0.06",
                  "costEstimate": "1.96",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T01:30:00+00:00",
                  "value": "0.06",
                  "costEstimate": "1.96",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T02:00:00+00:00",
                  "value": "0.10",
                  "costEstimate": "3.28",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T02:30:00+00:00",
                  "value": "0.16",
                  "costEstimate": "5.25",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T03:00:00+00:00",
                  "value": "0.15",
                  "costEstimate": "4.93",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T03:30:00+00:00",
                  "value": "0.25",
                  "costEstimate": "8.22",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T04:00:00+00:00",
                  "value": "0.28",
                  "costEstimate": "9.20",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T04:30:00+00:00",
                  "value": "0.28",
                  "costEstimate": "9.20",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T05:00:00+00:00",
                  "value": "0.29",
                  "costEstimate": "9.52",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T05:30:00+00:00",
                  "value": "0.26",
                  "costEstimate": "8.54",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T06:00:00+00:00",
                  "value": "0.23",
                  "costEstimate": "7.56",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T06:30:00+00:00",
                  "value": "0.17",
                  "costEstimate": "5.58",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T07:00:00+00:00",
                  "value": "0.25",
                  "costEstimate": "8.22",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T07:30:00+00:00",
                  "value": "0.28",
                  "costEstimate": "9.20",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T08:00:00+00:00",
                  "value": "0.22",
                  "costEstimate": "7.22",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T08:30:00+00:00",
                  "value": "0.22",
                  "costEstimate": "7.22",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T09:00:00+00:00",
                  "value": "0.18",
                  "costEstimate": "5.91",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T09:30:00+00:00",
                  "value": "0.07",
                  "costEstimate": "2.29",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T10:00:00+00:00",
                  "value": "0.07",
                  "costEstimate": "2.29",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T10:30:00+00:00",
                  "value": "0.07",
                  "costEstimate": "2.29",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T11:00:00+00:00",
                  "value": "0.06",
                  "costEstimate": "1.96",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T11:30:00+00:00",
                  "value": "0.06",
                  "costEstimate": "1.96",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T12:00:00+00:00",
                  "value": "0.07",
                  "costEstimate": "2.29",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T12:30:00+00:00",
                  "value": "0.06",
                  "costEstimate": "1.96",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T13:00:00+00:00",
                  "value": "0.12",
                  "costEstimate": "3.93",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T13:30:00+00:00",
                  "value": "0.07",
                  "costEstimate": "2.29",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T14:00:00+00:00",
                  "value": "0.16",
                  "costEstimate": "5.25",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T14:30:00+00:00",
                  "value": "0.25",
                  "costEstimate": "8.22",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T15:00:00+00:00",
                  "value": "0.22",
                  "costEstimate": "7.22",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T15:30:00+00:00",
                  "value": "0.21",
                  "costEstimate": "6.90",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T16:00:00+00:00",
                  "value": "0.21",
                  "costEstimate": "6.90",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T16:30:00+00:00",
                  "value": "0.21",
                  "costEstimate": "6.90",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T17:00:00+00:00",
                  "value": "0.20",
                  "costEstimate": "6.57",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T17:30:00+00:00",
                  "value": "0.25",
                  "costEstimate": "8.22",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T18:00:00+00:00",
                  "value": "0.29",
                  "costEstimate": "9.52",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T18:30:00+00:00",
                  "value": "0.27",
                  "costEstimate": "8.86",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T19:00:00+00:00",
                  "value": "0.26",
                  "costEstimate": "8.54",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T19:30:00+00:00",
                  "value": "0.26",
                  "costEstimate": "8.54",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T20:00:00+00:00",
                  "value": "0.26",
                  "costEstimate": "8.54",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T20:30:00+00:00",
                  "value": "0.26",
                  "costEstimate": "8.54",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T21:00:00+00:00",
                  "value": "0.26",
                  "costEstimate": "8.54",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T21:30:00+00:00",
                  "value": "0.26",
                  "costEstimate": "8.54",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T22:00:00+00:00",
                  "value": "0.25",
                  "costEstimate": "8.22",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T22:30:00+00:00",
                  "value": "0.16",
                  "costEstimate": "5.25",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T23:00:00+00:00",
                  "value": "0.05",
                  "costEstimate": "1.64",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                },
                {
                  "startAt": "2023-09-27T23:30:00+00:00",
                  "value": "0.04",
                  "costEstimate": "1.30",
                  "consumptionStep": 0,
                  "consumptionRateBand": "CONSUMPTION_STEPPED_03_02"
                }
              ]
            }
          ]
        }
      ]
    }
  }
}