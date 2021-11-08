# Star Cinema - Change Calculator App
## Overview
Due to the large queues of people waiting to get a ticket, Star Cinema has decided to develop an application to help cashiers speed up their job.

The application will return "SI" if the cahsier is able to give back customers the correct amount of change, otherwise it will return "NO".
The cashier is able to give back change if his cash register:
- Has the change amount or more
- Has currency denominations to make the exact amount of change

## Sample cases
| Input (queue of cusotmens)  | Output      |
| :-------------------------- | -----------:|
| [25, 25, 50]                | SI          |
| [25, 100]                   | NO          |
| [25, 25, 50, 50, 100]       | NO          |

**Notice:** As for today, it is assumed that cashier's initial amount of money in register is 0, and customers pay only with 25, 20 or 100 currency denominations.

## Run the application

