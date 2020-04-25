// Draw some text to the screen:
drawName('Ready to Code?');
// Animate the text!
bounceBubbles();

// Define color variables:
red = [0, 100, 63];
orange = [40, 100, 60];
green = [75, 100, 40];
blue = [196, 77, 55];
purple = [280, 50, 60];
letterColors = [red, orange, green, blue, purple];

// This variable controls the smallest distance at which a mouse will make the dots react
mouseResponseThreshold = 70;

// This variable controls how strongly the dots will try to return to their starting position
friction = 0.50;

// This variable controls how much the dots will rotate when interacting
rotationForce = 0.1;

message = 'Welcome to my first JS code!';

drawName(message, letterColors);
bounceBubbles();

//MATH OPERATIONS
console.log(Math.floor((Math.random()*100)));
console.log(Math.ceil(43.8));
console.log(Number.isInteger(2017));


