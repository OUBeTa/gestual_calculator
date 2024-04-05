In this project only the left hand model was used, so both your hands must be thumb right ( kinda dumb, ik :3 )

`|left hand : palm turned to webcam|`

`|right hand : palm turned to you|`

The program understand that your hands represents a 5 digits binary number each, reading thumb to pinky finger, so, thumb and middle finger up is gonna be read as: 00101, midle and index finger is read as: 00110

This calculator has support for two hands. When you turn on the calculator, each hand will have a number on te top of it, meaning their index. By pulling a hand in front of your cam you are registering an item in a LIFO list, witch means that the actual firts hand you pull will be turned into the hand number 1, and the second hand will be the hand number 0. last hand pulled will be the zero hand.

hand number 1 is responsible for the commands
hand number 0 is responsible for the numbers

here are the comands that i already made

| binary code | signal                | effect                    |
|:-----------:|:---------------------:|:-------------------------:|
| 0000100001  | both thumbs up        | start gestual reading     |
| 1111111111  | all fingers up        | ends gestual reading      |
| 10111       | ring finger down      | register a number         |
| 00111       | pinky and middle down | register negative numbers |
| 00011       | thumb and index up    | +                         |
| 00110       | index and middle up   | -                         |
| 10011       | middle and ring down  | *                         |
| 10110       | thumb and ring down   | /                         |
| 11110       | thumb down            | open parens               |
| 10001       | thumb and pinky up    | close parens              |
| 00001       | thumb up              | erase                     |
| 10000       | pinky up              | decimal point             |
| 11111       | all five fingers up   | output results            |

`Remember to keep your hands with your thumbs poiting both to your right`

all actions above that have 5 bits are for hand number 1, hand number 0 only say numbers in binary. The 10 bits codes are for dual hand signals 

"True table" for 5 + (3 * (-5 / 2.4)) - 19

| lines | hand0 code | hand1 code | hand0 signal | hand1 signal      | dual hand signal | operation                    |
|:-----:|:----------:|:----------:|:------------:|:-----------------:|:----------------:|:-----------------------------|
| 1     | 00001      | 00001      | ERASE        | ERASE             | START            | ""                           |
| 2     | 00101      | 10111      | NONE         | REGISTER          | NONE             | "5"                          |
| 3     | 00000      | 00011      | NONE         | ADD               | NONE             | "5 + "                       |
| 4     | 00000      | 11110      | NONE         | PARENS_OPEN       | NONE             | "5 + ("                      |
| 5     | 00011      | 10111      | ADD          | REGISTER          | NONE             | "5 + (3"                     |
| 6     | 00000      | 10011      | NONE         | MULT              | NONE             | "5 + (3 * "                  |
| 7     | 00000      | 11110      | NONE         | PARENS_OPEN       | NONE             | "5 + (3 * ("                 |
| 8     | 00101      | 00111      | NONE         | REGISTER_NEGATIVE | NONE             | "5 + (3 * (-5"               |
| 9     | 00000      | 10110      | NONE         | DIV               | NONE             | "5 + (3 * ( -5 / "           |
| 10    | 00010      | 10111      | NONE         | REGISTER          | NONE             | "5 + (3 * (-5 / 2"           |
| 11    | 00000      | 10000      | NONE         | DECIMAL           | NONE             | "5 + (3 * (-5 / 2."          |
| 12    | 00100      | 10111      | NONE         | REGISTER          | NONE             | "5 + (3 * (-5 / 2.4"         |
| 13    | 00000      | 10001      | NONE         | PARENS_CLOSE      | NONE             | "5 + (3 * (-5 / 2.4) "       |
| 14    | 00000      | 10001      | NONE         | PARENS_CLOSE      | NONE             | "5 + (3 * (-5 / 2.4) )"      |
| 15    | 00000      | 00110      | NONE         | SUB               | NONE             | "5 + (3 * (-5 / 2.4) ) - "   |
| 16    | 10011      | 10111      | MUL          | REGISTER          | NONE             | "5 + (3 * (-5 / 2.4) ) - 19" |
| 17    | 00000      | 11111      | NONE         | OUT               | NONE             | "5 + (3 * (-5 / 2.4) ) - 19" |
| 18    | 11111      | 11111      | OUT          | OUT               | END              | ""                           |

 What we expect to happend in line 19 is the value -20.25 to be printed

# powered by : oub3t4 #