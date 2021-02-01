# API REST Calculadora

**URL Params**
   
    `param1: 6`
    `param2: 2`

## Suma 

# GET /calc/suma/{param1}/{param2}
+ Response 200 OK (application/json)
```json
[
        {
            "resultat": 8
        }
]        
```

## Resta 

# GET /calc/resta/{param1}/{param2}
+ Response 200 OK (application/json)
```json
[
        {
            "resultat": 4
        }
]        
```

## Multiplicació 

# GET /calc/multiplicacio/{param1}/{param2}
+ Response 200 OK (application/json)
```json
[
        {
            "resultat": 12
        }
]        
```

## Divisió 

# GET /calc/divisio/{param1}/{param2}
+ Response 200 OK (application/json)
```json
[
        {
            "resultat": 3
        }
]        
```