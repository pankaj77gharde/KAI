class ConfigData:
    OPEN_AI_KEY = "sk-proj-zMT3BlbkFJvo5yE7LutvHgPM-rFl8J27LfW3yAfw_Yw7c7ONWPIYVGMK4A"
    MONGO_DB_URI = "mongodb://localhost:27017/"
    DB_NAME = "db_test"
    HUGGINGFACE_API_TOKEN = "hf_SDmzzzykPUvExzfLgzCKNBIIN"
    
    # VOYAGE INFORMETION
    COLLECTION_NAME_VOYAGE = "VoyageRange"
    TABLE_SCHEMA_VOYAGE = '''
                    "version": "number",
                    "voyageId": "string",
                    "voyageNumber": "string",
                    "vesselName": "string",
                    "vesselImo":  "string",
                    "vesselId": "string",
                    "startDateUtc": "string (date-time)",
                    "endDateUtc": "string (date-time)",
                    "moduleType": "string",
                    "offhireDays": "number",
                    "tags": "string",
                    "url": "string",
                    "isEstimate": "boolean",
                    
                    "results": 
                        "bunkers": "number",
                        "commission": "number",
                        "days": "number",
                        "efficiency": "number",
                        "expense": "number",
                        "expenses": "number",
                        "modifiedByFull": "string",
                        "modifiedDate": "string (date-time)",
                        "pnl": "number",
                        "port": "number",
                        "revenue": "number",
                        "sailedIn": "number",
                        "tce": "number",
                        "resultDetail": [
                                 "classificationName": "string",
                                  "classificationTotal": "number" 
                                 ],

                    "resultsWhenFixed": 
                        "bunkers": "number",
                        "commission": "number",
                        "days": "number",
                        "efficiency": "number",
                        "expense": "number",
                        "expenses": "number",
                        "modifiedByFull": "string",
                        "modifiedDate": "string (date-time)",
                        "pnl": "number",
                        "port": "number",
                        "revenue": "number",
                        "sailedIn": "number",
                        "tce": "number",
                        "resultDetail": [
                                  "classificationName": "string",
                                  "classificationTotal": "number" 
                                  ],

                    "fixtureList": 
                    [
                        "cpDate": "string (date-time)",
                        "cpQuantity": "number",
                        "demurrage": "number",
                        "displayOrder": "number",
                        "fixtureNumber": "string",
                        "fixtureRemark": "string",
                        "grades": "string",
                        "layCanDateEnd": "string (date-time)",
                        "layCanDateStart": "string (date-time)",
                        "laytime": "number",
                        "otherTimeBar": "number",
                        "overage": "number",
                        "timeBar": "number",
                        
                        "fixtureBillsOfLading": [
                        "billOfLadingDate": "string (date-time)",
                        "description": "string",
                        "displayOrder": "number",
                        "fixtureGradeName": "string",
                        "portName": "string",
                        "fixturePortLinkToken": "string",
                        "quantityBBLS": "number",
                        "quantityMT": "number",
                        "shipper": "string",
                        "loadPortID": "number",
                        "dischargePortID": "number"
                        ],

                        "fixtureCommissions": [
                        "commissionType": "string",
                        "organizationGroupName": "string",
                        "organizationName": "string",
                        "organizationExternalId": "string",
                        "rate": "number"
                        ],

                        "fixtureGrades": [
                        "displayOrder": "number",
                        "gradeName": "string"
                        ],

                        "fixturePorts": [
                        "portId": "number",
                        "portName": "string",
                        "displayOrder": "number",
                        "activityType": "string",
                        "fixturePortLinkToken": "string"
                        ],

                        "fixtureRevenueList": [
                        "accrual": "number",
                        "displayOrder": "number",
                        "fixtureDisplayOrder": "number",
                        "flatRate": "number",
                        "isCommission": "boolean",
                        "name": "string",
                        "quantity": "number",
                        "remark": "string",
                        "total": "number",
                        "totalAccrued": "number",
                        "ws": "number"
                        ],

                        "fixtureExpenseList": [
                        "amount": "number",
                        "daily": "boolean",
                        "displayOrder": "number",
                        "fixtureDisplayOrder": "number",
                        "name": "string",
                        "remark": "string",
                        "total": "number"
                        ]
                        
                        "tags": "string",
                        "tagList":[
                            "category":"string",
                            "value":"string",
                                ]
                    ],

                    "legList": 
                    [
                        "arriveActualized": "boolean",
                        "arriveDraftFore": "number",
                        "arriveDraftAft": "number",
                        "arriveFw": "number",
                        "arriveSlops": "number",
                        "arriveUtc": "string (date-time)",
                        "arriveLocal": "string (date-time)",
                        "awaitingLaycanDays": "number",
                        "cleaningDay": "number",
                        "cost": "number",
                        "departActualized": "boolean",
                        "departDraftAft": "number",
                        "departDraftFore": "number",
                        "departFw": "number",
                        "departSlops": "number",
                        "departUtc": "string (date-time)",
                        "departLocal": "string (date-time)",
                        "displayOrder": "number",
                        "distanceEca": "number",
                        "distanceEcaPercent": "number",
                        "distanceNonEca": "number",
                        "distanceTotal": "number",
                        "fixturePortLinkToken": "string",
                        "heatingRatio": "number",
                        "isBunkering": "boolean",
                        
                        "bunkerStemsList": "array of strings",

                        "bunkerROBList": [
                        "bunkerGradeName": "string",
                        "arrivalROBQuantity": "number",
                        "departureROBQuantity": "number"
                        ],

                        "isTCODelivery": "boolean",
                        "isTCORedelivery": "boolean",
                        "passageDays": "number",
                        "portId": "number",
                        "portName": "string",
                        "portRegulation": "string",
                        "portShortName": "string",
                        "portTimeZone": "number",
                        "speed": "number",
                        "timeZoneArrive": "number",
                        "timeZoneDepart": "number",
                        "totalPortDays": "number",
                        "type": "string",
                        "wx": "number",
                        "voyageLegId": "string"
                    ],

                    "revenueList": [
                        "accrual": "number",
                        "displayOrder": "number",
                        "fixtureDisplayOrder": "number",
                        "flatRate": "number",
                        "isCommission": "boolean",
                        "name": "string",
                        "quantity": "number",
                        "remark": "string",
                        "total": "number",
                        "totalAccrued": "number",
                        "ws": "number"
                        ],
                        
                    "expenseList": [
                        "amount": "number",
                        "daily": "boolean",
                        "displayOrder": "number",
                        "fixtureDisplayOrder": "number",
                        "name": "string",
                        "remark": "string",
                        "total": "number",
                        ],

                    "bunkerList": [
                        "averageConsumptionCost": "number",
                        "bunkerGradeName": "string", 
                        "consCost": "number",
                        "consTotal": "number",
                        "displayOrder": "number",
                        "refillPrice": "number",
                        "remainderConsCost": "number",
                        "totalCost": "number"
                    ],

                    "emissionsDetails": 
                        "voyageCIIBand": "string",
                        "voyageCO2": "number",
                        "voyageEEOI": "number",
                        "voyageAER": "number",
                        "voyageSOxMt": "number",
                        "voyageSOx": "number",
                        "voyageNOxMt": "number",
                        "voyageNOx": "number",
                        
                        "euEtsDetails": 
                            "allowancePurchases":"array of strings",
                            "eua":"number",
                            "euaCostUSD":"number",
                            "euaCostEUR":"number",
                            "euaPriceUSD":"number",
                            "euaPriceEUR":"number",
                            "euaVerified":"number",
                            "euaEstimated":"number",
                            "euaPurchased":"number",
                            "euaBalance":"number"
                            
                        "legEmissionsDetails": [
                            "portName":"string",
                            "displayOrder":"number",
                            "co2":"number",
                            "eeoi":"number",
                            "aer":"number",
                            "soxMt":"number",
                            "sox":"number",
                            "noxMt":"number",
                            "nox":"number",
                            "euEtsDetails":
                                "allowancePurchases":"array of strings",
                                "eua":"number",
                                "euaCostUSD":"number",
                                "euaCostEUR":"number",
                                "euaPriceUSD":"number",
                                "euaPriceEUR":"number",
                                "euaVerified":"number",
                                "euaEstimated":"number",
                                "euaPurchased":"number",
                                "euaBalance":"number", 
                                ],

                    "remarkList": [
                        "modifiedDate": "string (date-time)",
                        "modifiedByFull": "string",
                        "remark": "string"
                    ],

                    "offhireList":
                        [
                            'id': "number", 
                            'dateStartUtc': "string (date-time)",
                            'dateEndUtc': "string (date-time)",
                            'days': "number", 
                            'displayOrder':"number", 
                            'offhireReason': "string" 
                            'remark': "string"
                            'offhireBunkerList': [
                                'id': "number", 
                                'gradeName': "string"
                                'quantity': "number", 
                                'price': "number", 
                                'displayOrder': "number"
                                ]
                        ],
                    
                    "tcNumber": "string",
                    "tcOutIdEncrypted": "string",
                    "tcReletDetail": "object",
                    "source_file": "string",
                    '''
    
    SCHEMA_DESCRIPTION_VOYAGE = '''
                    Here is the description to determine what each key represents:
                    1. _id:
                        - Description: Unique identifier for the document.  
                    2. version:
                        - Description: Version number of the document schema.
                    3. voyageId:
                        - Description: Unique identifier for the voyage.
                    4. voyageNumber:
                        - Description: Human-readable voyage reference number.
                    5. vesselName:
                        - Description: Name of the vessel.
                    6. vesselImo:
                        - Description: International Maritime Organization number of the vessel.
                    7. vesselId:
                        - Description: Unique identifier for the vessel.
                    8. startDateUtc:
                        - Description: UTC start date/time of the voyage.
                    9. endDateUtc:
                        - Description: UTC end date/time of the voyage.
                    10. moduleType:
                        - Description: Type of voyage module (e.g., "Spot").
                    11. offhireDays:
                        - Description: Number of days vessel was off hire.
                    12. tags:
                        - Description: String of categorization tags for the voyage
                    13. url:
                        - Description: Reference URL for the voyage in the system.
                    14. isEstimate:
                        - Description: Total estimated values 
                    15. results:
                        - Description: Financial and operational results of the voyage
                        - Fields:
                            - bunkers:
                                - Description: Cost of bunkers (fuel).
                            - commission:
                                - Description: Total commission costs.
                            - days:
                                - Description: Total duration of voyage in days.
                            - efficiency:
                                - Description: Operational efficiency metric.
                            - expenses:
                                - Description: Total expenses for the voyage.
                            - modifiedByFull:
                                - Description: Name of the person who last modified the voyage record
                            - modifiedDate:
                                - Description: Timestamp indicating when the voyage record was last modified
                            - pnl:
                                - Description: Profit and Loss figure.
                            - port:
                                - Description: Total port-related costs for the voyage
                            - revenue:
                                - Description: Total revenue generated.
                            - sailedIn:
                                - Description: Total operational costs while the vessel was sailing
                            - tce:
                                - Description: Time Charter Equivalent rate.
                            - resultDetail:
                                - Description: Array of revenue classifications
                                - Fields:
                                    - classificationName:
                                        - Description: Type of revenue (e.g., Freight, Dem).
                                    - classificationTotal:
                                        - Description: Total amount for that classification.
                    16. fixtureList :
                        - cpDate:
                            - Description: Charter Party agreement date
                        - cpQuantity:
                            - Description: Contracted quantity of cargo
                        - demurrage:
                            - Description: Rate charged for detention of vessel beyond agreed laytime
                        - displayOrder:
                            - Description: Sorting order for display purposes
                        - fixtureNumber:
                            - Description: Unique reference number for the fixture
                        - grades:
                            - Description: Type/grade of cargo to be carried
                        - layCanDateStart/End:
                            - Description: Laycan window (earliest and latest dates for vessel presentation)
                        - laytime:
                            - Description: Allowed time for loading/discharging operations
                        - otherTimeBar:
                            - Description: Additional time allowance separate from standard laytime
                        - overage:
                            - Description: Amount of cargo loaded in excess of the contracted quantity
                        - timeBar:
                            - Description: Time limit for submitting claims related to the voyage
                        - fixtureBillsOfLading:
                            - Description: Array of bill of lading documents
                            - Fields:
                                - billOfLadingDate:
                                    - Description: Date when the Bill of Lading was issued
                                - description:
                                    - Description: Textual description of the cargo
                                - displayOrder:
                                    - Description: Numerical order for display purposes
                                - fixtureGradeName:
                                    - Description: Grade/type of cargo as specified in the fixture
                                - portName:
                                    - Description: Name of the port associated with the Bill of Lading
                                - fixturePortLinkToken:
                                    - Description: Unique identifier linking port to specific fixture
                                - quantityBBLS:
                                    - Description: Cargo quantity in barrels
                                - quantityMT:
                                    - Description: Cargo quantity in metric tons
                                - shipper:
                                    - Description: Entity responsible for shipping the cargo
                                - loadPortID:
                                    - Description: Unique identifier for the loading port
                                - dischargePortID:
                                    - Description: Unique identifier for the discharge port
                                - voyageFixtureGradeDisplayOrder: 
                                    - Description: display garde order
                        - fixtureCommissions:
                            - Description: Array of commission entries for different parties involved in the fixture
                            - Fields:
                                - commissionType:
                                    - Description: Category/role of the commission recipient
                                - organizationGroupName:
                                    - Description: Parent company or group name
                                - organizationName:
                                    - Description: Specific company/entity name receiving commission
                                - organizationExternalId:
                                    - Description: External reference number for the organization
                                - rate:
                                    - Description: Commission percentage rate
                        - fixtureGrades:
                            - Description: Array containing cargo grade specifications for the fixture
                            - Fields:
                                - displayOrder:
                                    - Description: Numerical order for display sequencing
                                - gradeName:
                                    - Description: Name or code of the cargo grade
                        - fixturePorts:
                            - Description: Array containing sequence of ports involved in the fixture
                            - Fields:
                                - portId:
                                    - Description: Unique identifier for the port in the system
                                - portName:
                                    - Description: Name of the port
                                - displayOrder:
                                    - Description: Sequential order of ports in the voyage
                                - activityType:
                                    - Description: Type of operation at the port
                                - fixturePortLinkToken:
                                    - Description: Unique identifier linking port to specific fixture
                        - fixtureRevenueList:
                            - Description: Object representing the main freight revenue for the fixture
                            - Fields:
                                - accrual:
                                    - Description: Amount to be accrued for accounting periods
                                - displayOrder:
                                    - Description: Position in display sequence
                                - fixtureDisplayOrder:
                                    - Description: Order within specific fixture context
                                - flatRate:
                                    - Description: Base freight rate for the cargo
                                - isCommission:
                                    - Description: Indicates if subject to commission calculations
                                - name:
                                    - Description: Revenue type identifier
                                - quantity:
                                    - Description: Quantity basis for freight calculation
                                - remark:
                                    - Description: Additional information about freight terms
                                - total:
                                    - Description: Total freight amount
                                - totalAccrued:
                                    - Description: Total amount accrued to date
                                - ws:
                                    - Description: Worldscale rate reference
                        - fixtureExpenseList:
                            - Description: Array of expense items associated with the fixture
                            - Fields:
                                - amount:
                                    - Description: Base amount for the expense item
                                - daily:
                                    - Description: Indicates if expense is calculated on a daily basis
                                - displayOrder:
                                    - Description: Sequence number for display purposes
                                - fixtureDisplayOrder:
                                    - Description: Order within specific fixture context
                                - name:
                                    - Description: Type/category of expense
                                - remark:
                                    - Description: Additional information about expense
                                - total:
                                    - Description: Final amount for the expense item
                            - tags:
                                - Description: String containing categorization tags for the fixture
                        - tagList:
                            - Description: Object containing categorization metadata for the fixture
                            - Fields:
                                - category:
                                    - Description: Type/classification of the tag
                                - value:
                                    - Description: Specific value within the category
                    17. legList:
                        - arriveActualized:
                            - Description: Flags indicating if arrival data is actual
                        - arriveDraftFore:
                            - Description: Vessel draft measurements on arrival
                        - arriveDraftAft:
                            - Description: Vessel draft measurements on arrival
                        - arriveFw:
                            - Description: Fresh water quantity on arrival
                        - arriveSlops:
                            - Description: Slops quantity on arrival
                        - arriveUtc:
                            - Description: UTC timestamps for arrival
                        - arriveLocal:
                            - Description: Local timestamps for arrival
                        - awaitingLaycanDays:
                            - Description: waiting days for arrival
                        - cleaningDay:
                            - Description: vessel cleaning days 
                        - cost:
                            - Description: vessel cleaning cost
                        - departActualized:
                            - Description: Flags indicating if departure data is actual
                        - departDraftAft:
                            - Description: Vessel draft measurements on departure
                        - departDraftFore:
                            - Description: Vessel draft measurements on departure
                        - departFw:
                            - Description: Fresh water quantity on departure
                        - departSlops:
                            - Description: Slops quantity on departure
                        - departUtc:
                            - Description: UTC timestamps for departure
                        - departLocal:
                            - Description: Local timestamps for departure
                        - displayOrder:
                            - Description: Sequence number for display purposes
                        - distanceEca:
                            - Description: Distance in Emission Control Areas
                        - distanceEcaPercent:
                            - Description: percentage distance in Emission Control Areas
                        - distanceNonEca:
                            - Description: Distance outside ECAs
                        - distanceTotal:
                            - Description: Total distance for leg
                        - fixturePortLinkToken:
                            - Description: Unique identifier linking port to specific fixture
                        - heatingRatio:
                            - Description: heating retio in vessel 
                        - isBunkering:
                            - Description: fuel availble or not  
                        - bunkerStemsList: 
                            -Description: Array of bunkering operations
                        - isTCODelivery:
                            - Description: Time Critical Option Deliver) typically refers to a specialized shipping service designed for time-sensitive or urgent deliveries.
                        - isTCORedelivery:
                            - Description: Time Critical Option Redelivery) typically refers to a second or subsequent delivery attempt for a time-critical shipment.
                        - passageDays:
                            - Description: number of days that have elapsed since a specific shipping event or milestone
                        - portId:
                            - Description: Unique identifier for port
                        - portName:
                            - Description: name of port
                        - portRegulation:
                            - Description: Regulatory zone of port
                        - portShortName:
                            - Description: Full and abbreviated port names
                        - portTimeZone:
                            - Description: Port time zone offset
                        - speed:
                            - description: Average speed during leg
                        - timeZoneArrive:
                            - Description: arrival time 
                        - timeZoneDepart:
                            - Description: Departure time 
                        - totalPortDays:
                            - Description: number of days at port
                        - type:
                            - Description: Indicates the operational activity type at the port
                        - wx:
                            - Description: Weather factor
                        - voyageLegId:
                            - Description: Unique identifier for specific voyage leg
                        - bunkerROBList:
                            - Description: Remaining on board bunker quantities.
                            - Fields:
                                - bunkerGradeName:
                                    - Description: Type of bunker fuel.
                                - arrivalROBQuantity:
                                    - Description: Quantity on arrival
                                - departureROBQuantity:
                                    - Description: Quantity on departure
                    18. revenueList:
                        - accrual:
                            - Description: Accrued amount for revenue item if different from total
                        - displayOrder:
                            - Description: Sequential number for ordering revenue items
                        - fixtureDisplayOrder:
                            - Description: Order number relating to specific fixture
                        - flatRate:
                            - Description: Base rate for revenue calculation
                        - isCommission:
                            - Description: Indicates if item is commission-related
                        - name:
                            - Description: Type/name of revenue item
                        - quantity:
                            - Description: Volume or amount used for revenue calculation
                        - remark:
                            - Description: Additional notes about revenue item
                        - total:
                            - Description: Total calculated revenue amount
                        - totalAccrued:
                            - Description: Total amount actually accrued
                        - ws:
                            - Description: Worldscale rate if applicable
                    19. expenseList:
                        - amount:
                            - Description: Base amount for the expense
                        - daily:
                            - Description: Indicates if expense is charged daily
                        - displayOrder:
                            - Description: Sequence number for display ordering
                        - fixtureDisplayOrder:
                            - Description: Links expense to specific fixture order
                        - name:
                            - Description: Name/type of expense
                        - remark:
                            Description: Additional notes about the expense
                        - total:
                            - Description: Final calculated expense amount
                    20. bunkerList:
                        - averageConsumptionCost:
                            - Description: Average cost per unit of fuel consumed
                        - bunkerGradeName:
                            - Description: Grade/type of bunker fuel
                        - consCost:
                            - Description: Total cost of consumed fuel
                        - consTotal:
                            - Description: Total quantity of fuel consumed
                        - displayOrder:
                            - Description: Sequence number for display ordering
                        - refillPrice:
                            - Description: Unit price for fuel replenishment
                        - remainderConsCost:
                            - Description: Cost of remaining unused fuel
                        - totalCost:
                            - Description: Total cost including consumption and remainder
                    21. emissionsDetails:
                        - voyageCIIBand:
                            - Description: Carbon Intensity Indicator rating band
                        - voyageCO2:
                            - Description: Total CO2 emissions for the voyage
                        - voyageEEOI:
                            - Description: Energy Efficiency Operational Indicator
                        - voyageAER:
                            - Description: Annual Efficiency Ratio
                        - voyageSOxMt:
                            - Description: Sulfur Oxide emissions in metric tons
                        - voyageSOx:
                            - Description: Sulfur Oxide emissions ratio
                        - voyageNOxMt:
                            - Description: Nitrogen Oxide emissions in metric tons
                        - voyageNOx:
                            - Description: Nitrogen Oxide emissions ratio
                        - legEmissionsDetails:
                            - Description: Array containing emissions data per voyage leg
                            - Fields:
                                - portName:
                                    - Description: Name of the port for this leg
                                - displayOrder:
                                    - Description: Sequence number for ordering legs
                                - co2:
                                    - Description: Carbon dioxide emissions for the leg
                                - eeoi:
                                    - Description: Energy Efficiency Operational Indicator for leg
                                - aer:
                                    - Description: Annual Efficiency Ratio for leg
                                - soxMt:
                                    - Description: Sulfur oxide emissions in metric tons
                                - sox:
                                    Description: Sulfur oxide emissions ratio
                                - noxMt:
                                    - Description: Nitrogen oxide emissions in metric tons
                                - nox:
                                    - Description: Nitrogen oxide emissions ratio
                                - euEtsDetails:
                                    - Description: EU Emissions Trading System details and transactions
                    22. remarkList:
                        - modifiedDate:
                            - Description: Timestamp of when remark was last modified
                        - modifiedByFull:
                            - Description: Full name of person who modified the remark
                        - remark:
                            - Description: Actual content of the remark
                    23. offhireList:
                        - id:
                            - Description: Unique identifier for off-hire record
                        - dateStartUtc:
                            - Description: Start date/time of off-hire period in UTC
                        - dateEndUtc:
                            - Description: End date/time of off-hire period in UTC
                        - days:
                            - Description: Duration of off-hire period in days
                        - displayOrder:
                            - Description: Sequence number for display ordering
                        - offhireReason:
                            - Description: Reason for vessel being off-hire
                            Type: String/Null
                        - remark:
                            Description: Additional notes about off-hire period
                        - offhireBunkerList:
                            - Description: Array of bunker details during off-hire
                            - Fields:
                                - id:
                                    - Description: Unique identifier for bunker record
                                - gradeName:
                                    - Description: Grade/type of bunker fuel
                                - quantity:
                                    - Description: Amount of fuel
                                - price:
                                    - Description: Price per unit of fuel
                                - displayOrder:
                                    - Description: Sequence for display
                    24. tcNumber:
                        - Description: Time Charter contract reference number
                    25. tcOutIdEncrypted:
                        - Description: Encrypted identifier for time charter out contract
                    26. tcReletDetail:
                        - Description: Details about vessel relet arrangements 
                    27. "source_file": 
                        - Description: Name of the json file having all the details
                    '''
    FEW_SHOT_EXAMPLE_1_VOYAGE = [
                            {
                            "$match": {
                                "vesselName": "Stena Performance"
                            }
                            },
                            {
                            "$project": {
                                "route": {
                                "$concat": [
                                    "$results.loadPort",
                                    " -> ",
                                    "$results.dischargePort"
                                ]
                                },
                                "voyageId": 1,
                                "voyageNumber": 1,
                                "bunkerCosts": "$bunkerList",
                                "expenses": "$expenseList",
                                "startDate": "$startDateUtc",
                                "endDate": "$endDateUtc"
                            }
                            },
                            {
                            "$addFields": {
                                "totalBunkerCost": {
                                "$sum": "$bunkerList.amount"
                                },
                                "totalExpenses": {
                                "$sum": "$expenseList.amount"
                                }
                            }
                            },
                            {
                            "$project": {
                                "route": 1,
                                "voyageId": 1,
                                "voyageNumber": 1,
                                "startDate": 1,
                                "endDate": 1,
                                "totalBunkerCost": 1,
                                "totalExpenses": 1,
                                "totalCost": {
                                "$add": ["$totalBunkerCost", "$totalExpenses"]
                                },
                                "costDetails": {
                                "bunker": "$bunkerCosts",
                                "expenses": "$expenses"
                                }
                            }
                            },
                            {
                            "$sort": {
                                "startDate": 1
                            }
                            }
                        ]
    
    # VOYAGE INFORMETION
    COLLECTION_NAME_VESSEL = "VesselRegisterDetailRange"
    TABLE_SCHEMA_VESSEL = '''
                            "vesselId": "string",
                            "name": "string",
                            "imo": "string",
                            "accountCode": "string",
                            "hireRate": "number",
                            "mastersEmail": "string",
                            "scrubber": "string",
                            "isVesselOperating": "boolean",
                            "marketType": "string",
                            "source_file": "string",
                            
                            "profileList": 
                                "profileName": "string",
                                "passageProfile": 
                                    "passageType": "string",
                                    "consumption": 
                                        "rpm": "number",
                                        "ifo": "number",
                                        "mgo": "number",
                                        "speed": "number",
                                        "isDefault": "boolean",
                                "nonPassageProfile": 
                                    "consumption": 
                                        "ifoLoad": "number",
                                        "ifoDischarge": "number",
                                        "ifoIdle": "number",
                                        "ifoHeat": "number",
                                        "ifoClean": "number",
                                        "ifoInert": "number",
                                        "mgoLoad": "number",
                                        "mgoDischarge": "number",
                                        "mgoIdle": "number",
                                        "mgoHeat": "number",
                                        "mgoClean": "number",
                                        "mgoInert": "number",
                            "tagList": 
                                "category": "string",
                                "value": "string"
                            "headContract": 
                                "list": 
                                    "tcInIdEncrypted": "string",
                                    "displayOrder": "number",
                                    "contractNumber": "string",
                                    "owner": "string",
                                    "cpDate": "string",
                                    "deliveryDatetime": "string",
                                    "duration": "number",
                                    "durationType": "string",
                                    "option": "string",
                                    "isCurrent": "boolean"
                    '''
    
    SCHEMA_DESCRIPTION_VESSEL = '''
                    Here is the description to determine what each key represents:
                    1. _id:
                        - Description: Unique identifier for the document.  
                    2. vesselId:
                        - Description: Unique identifier for the vessel
                    3. name:
                        - Description: Vessel's registered name
                    4. imo:
                        - Description: International Maritime Organization number
                    5. accountCode:
                        - Description: Internal accounting reference code
                    6. hireRate:
                        - Description: Daily hire rate for the vessel
                    7. mastersEmail:
                        - Description: Email address of vessel's master
                    8. scrubber:
                        - Description: Type/status of emission scrubber system
                    9. isVesselOperating:
                        - Description: Current operational status
                    10. marketType:
                        - Description: Market segment vessel operates in
                         
                    11. profileList:
                        - Description: Vessel performance profiles
                        - Fields:
                            - profileName:
                                - Description: Name of performance profile
                            - passageProfile:
                                - passageType:
                                    - Description: Type of passage
                                - consumption:
                                    - rpm: 
                                        - Description: Engine RPM
                                    - ifo: 
                                        - Description: IFO consumption
                                    - mgo: 
                                        - Description: MGO consumption
                                    - speed: 
                                        - Description: Vessel speed
                                    - isDefault: 
                                        - Description: Default profile flag
                            - nonPassageProfile:
                                - Description: Consumption during non-passage activities
                                - Fields:
                                    - consumption:
                                        - ifoLoad:
                                            - Description: IFO consumption during cargo loading operations
                                        - ifoDischarge:
                                            - Description: IFO consumption during cargo discharge operations
                                        - ifoIdle:
                                            - Description: IFO consumption while vessel is idle/waiting
                                        - ifoHeat:
                                            - Description: IFO consumption for cargo heating operations
                                        - ifoClean:
                                            - Description: IFO consumption during tank cleaning operations
                                        - ifoInert:
                                            - Description: IFO consumption for tank inerting operations
                                        - mgoLoad:
                                            - Description: MGO consumption during cargo loading operations
                                        - mgoDischarge:
                                            - Description: MGO consumption during cargo discharge operations
                                        - mgoIdle:
                                            - Description: MGO consumption while vessel is idle/waiting
                                        - mgoHeat:
                                            - Description: MGO consumption for cargo heating operations
                                        - mgoClean:
                                            - Description: MGO consumption during tank cleaning operations
                                        - mgoInert:
                                            - Description: MGO consumption for tank inerting operations
                    12. fixtureList :
                        - tagList:
                            - Description: Categorization tags
                            - Fields:
                                - category:
                                    - Description: Tag category name
                                - value:
                                    - Description: Tag value
                    13. headContract:
                        - Description: Primary charter contract details
                        - Fields:
                            - list:
                                - tcInIdEncrypted:
                                    - Description: Encrypted time charter ID
                                - displayOrder:
                                    - Description: Contract display sequence
                                - contractNumber:
                                    - Description: Contract reference number
                                - owner:
                                    - Description: Vessel owner name
                                - cpDate:
                                    - Description: Charter party date
                                - deliveryDatetime:
                                    - Description: Vessel delivery date/time
                                - duration:
                                    - Description: Contract duration
                                - durationType:
                                    - Description: Unit of duration measurement
                                - option:
                                    - Description: Contract extension options
                                - isCurrent:
                                    - Description: Active contract flag
                    14. tcReletDetail:
                        - Description: Details about vessel relet arrangements 
                    '''
    FEW_SHOT_EXAMPLE_1_VESSEL = [
                        {
                        "$match": {"name": "Stena Image"}
                        },
                        {
                        "$unwind": "$headContract.list"
                        },
                        {
                        "$match": {
                            "headContract.list.deliveryDatetime": {
                            "$gte": {"$date": "2020-06-07T00:00:00.000Z"}
                            }
                        }
                        },
                        {
                        "$project": {
                            "_id": 0,
                            "vesselName": "$name",
                            "contractNumber": "$headContract.list.contractNumber",
                            "earnings": "$headContract.list.earningResults"
                        }
                        }
                    ] 
    
    EMAIL_EXAMPLE = '''
                    Its text file with details explnetion.follwing are the important topics for email data. :
                    1. FROM,
                    2. TO, 
                    3. DATE,
                    4. SUBJECT,
                    5. VOYAGE DETAILS,
                    6. FINANCIAL METRICS,
                    7. VOYAGE SPECIFICATIONS,
                    8. OPERATIONAL COMMENTS,
                    9. IMPROVEMENTS,
                    10. FIXTURE COMMENTS
                   '''
                   
    VOYAGE_EXAMPLE = '''
                    Its JSON file in keys and values or nested dictonry with int, str, flot, etc data.follwing are the important topics for voyage data.:
                    1. _id,  
                    2. version,
                    3. voyageId,
                    4. voyageNumber,
                    5. vesselName,
                    6. vesselImo,
                    7. vesselId,
                    8. startDateUtc,
                    9. endDateUtc,
                    10. moduleType,
                    11. offhireDays,
                    12. tags,
                    13. url,
                    14. isEstimate,
                    15. results,
                    16. fixtureList,
                    17. legList,
                    18. revenueList,
                    19. expenseList,
                    20. bunkerList,
                    21. emissionsDetails,
                    22. remarkList,
                    23. offhireList,
                    24. tcNumber,
                    25. tcOutIdEncrypted,
                    26. tcReletDetail, 
                    27. source_file
                    '''
    VESSEL_EXAMPLE =  '''
                    Its JSON file in keys and values or nested dictonry with int, str, flot, etc data. Follwing are the important topics for vessel data. :
                    1. _id,
                    2. vesselId,
                    3. name,
                    4. imo:,
                    5. accountCode,
                    6. hireRate:,
                    7. mastersEmail,
                    8. scrubber:,
                    9. isVesselOperating,
                    10. marketType,
                    11. profileList,
                    12. fixtureList,
                    13. headContract,
                    14. tcReletDetail
                    '''
