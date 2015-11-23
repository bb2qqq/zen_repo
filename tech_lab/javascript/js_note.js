# GENERAL

### Strings

    // In JSON, only double quotes for string is accpeted, in any other cases in javascript, ' and " has no difference

    "string"

    "string".length     // Length property of a string

    // substring feature test
    "string".substring(2)
    'ring'

    "string".substring(0, 1)
    's'

    "string".substring(2, 0)
    'st'

    'I' + ' Wanna' + ' Fuck you'
    'I Wanna Fuck you'

    'a' + 5 // What?! string can add integer, oh my god!
    'a5'

    3*4/5               // Here the result is 2.4, which means js support float operation with integers

    // two forward slashes are used to comment in js

    /*
       This is the way how to comment multiple line in java.
       You got it?
    */


    confirm('This sites main containing two stupid fucking each other, you wanna continue?')            // pop out user confirm interface

    prompt('Javascript is fuckingly interesting, isn\'t it?')       // pop out an interactive prompt

    var age = prompt('tell me your age.')                           // Assign user_input to variable

    console.log("This is print?")           // js print function

// When comparing two values are equal or not, there are two types of compare operator, the ==/!= pair and ===/!== pair
// ==/!= will convert the type of the value if they are not the same type, ===/!== pair doesn't convert and do simple comparison

    1 == true
    true
    1 === true
    false

    2 != '2'
    false
    2 !== '2'
    true

// It looks that javascript doesn't support advance data-type comparison
    ['a'] == ['a']
    false
    ['a'] === ['a']
    false

    {'a': 1} == {'a': 1}
    false
    {'a': 1} === {'a': 1}
    false

### Variable

// var
// if in global scope, using var or not to def a variable is just the same, but inside a function, var will create a local variable,
// meanwhile 'no var' will look up the scope chain until it finds the variable or hits the global scope(at which point it will creat it):
// Below is an example from the internet: http://stackoverflow.com/questions/1470488/what-is-the-function-of-the-var-keyword-and-when-to-use-it-or-omit-it

    // These are both globals
    var foo = 1;
    bar = 2;

    function()
    {
        var foo = 1; // Local
        bar = 2;     // Global

        // Execute an anonymous function
        (function()
        {
            var wibble = 1; // Local
            foo = 2; // Inherits from scope above (creating a closure)
            moo = 3; // Global
        }())
    }



### CONDITION

    Im_your_father=1
    you_are_my_son=1
    if (Im_your_father) {
        console.log('go and suck my dicks');
    }
    else if ( you_are_my_son ) {
        console.log('shit shit shit');
    }
    else {
        console.log('oh, sorry, you just look the same like my son');
    }

### Functions
    var divideByThree = function (number) {
        var val = number / 3;
        console.log(val);
    };

    var greeting = function (you) {
        console.log('Fuck ' + you);      // seems ; can be omit here
    }

    // Here comes the magic undefined
    divideByThree()
    NaN
    divideByThree('qwe')
    NaN
    greeting()
    Fuck undefined

// Use Return
    var double_it = function(number) {
        return number * 2;
    };
    a = double_it(5)
    10

### Modules

    Math.random()
    0.9659100973512977


### jQuery
jQuery is a JavaScript library.
It makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers.
