# bonus_cards_testtask
django1.6.4 &amp; django rest 3.0.0 test task

API spec

1. GET /cards/ --> List of all cards
    query params allowed (search): series (серия), number (номер), status (статус), release_date (дата выпуска), activity_end_date (дата окончания активности)
response example: 
`
[
  {
    "id": 1,
    "series": 1,
    "number": 1,
    "release_date": "2017-11-11",
    "activity_end_date": "2021-11-11",
    "status": "not activated"
  }
]
`
2. GET /cards/{id}/ --> detail of the card
response example: 
`
{
    "id": 1,
    "series": 1,
    "number": 1,
    "release_date": "2017-11-11",
    "activity_end_date": "2021-11-11",
    "status": "not activated"
  }
`
3. POST /cards/ --> create new card
request body example: 
`
{
	"series": 1,
	"number": 1, 
	"release_date": "2017-11-11",
	"activity_end_date": "2021-11-11", 
	"status": "not activated",
	"usage_date": "2020-10-10"
}
`
response example: 
`
{
  "id": 2,
	"series": 1,
	"number": 1, 
	"release_date": "2017-11-11",
	"activity_end_date": "2021-11-11", 
	"status": "not activated"
}
`
4. DELETE /cards/{id} --> delete a card
