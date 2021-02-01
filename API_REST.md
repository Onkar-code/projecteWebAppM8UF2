# API REST Calculadora

## Suma [/calc/suma/{param1}/{param2}]

+ Parameters
    
    + param1: 6
    + param2: 2

### Result [GET]

+ Response 200 (application/json)

        {
            "resultat": 8
        }

## Resta [/calc/resta/{param1}/{param2}]

### Result [GET]

+ Response 200 (application/json)

    [
        {
            "resultat": 4
        }
    ]

## Multiplicació [/calc/multiplicacio/{param1}/{param2}]

### Result [GET]

+ Response 200 (application/json)

    [
        {
            "resultat": 12
        }
    ]


## Divisió [/calc/divisio/{param1}/{param2}]

### Result [GET]

+ Response 200 (application/json)

    [
        {
            "resultat": 3
        }
    ]