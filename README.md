# Star Cinema - Change Calculator App
Due to the large queues of people waiting to get a ticket, Star Cinema has decided to develop an application to help cashiers speed up their job.

The application will return "SI" if the cashier is able to give back customers the correct amount of change; otherwise, it will return "NO".
The cashier is able to give back change if his cash register:
- Has the necessary change amount or more
- Has currency denominations to make the exact amount of change

## Sample cases
| Input (queue of customers)  | Output      |
| :-------------------------- | -----------:|
| [25, 25, 50]                | SI          |
| [25, 100]                   | NO          |
| [25, 25, 50, 50, 100]       | NO          |

**Notice:** As for today, it is assumed that cashiers' initial amount of money in register is 0, and customers pay only with 25, 50 or 100 currency denominations.

## Requirements
In order to run this application ```Python 3.7``` is required. No third-party libraries are needed. 

## Running the application
Before you run the aplication, you may want to register some data about your customers in ```input.json```. Make sure that the format of your entries is correct.

Input sample format: 
```json
{
  "COLA_PAGO": [25, 25]
}
```

Make sure that:
- Input denominations are valid
- Inputs are integers

Run the application:

```console
$ python src/app.py
```

## Testing
### Run all tests
```console
$ python -m pytest
```
