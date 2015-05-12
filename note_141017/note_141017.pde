//work on processing
size(500, 500);
//255 * 255 is default size

//sky

//background(100);   //means background is grey
//sky color
background(200, 220, 255); //R, G, B

//ground

//ground color
//color(0, 120, 0);
//define line color
fill(0, 120, 0);
//define color to fill a shape, color() is not needed here actually after fill is defined
//color and fill won’t be changed for each shape drawn until overwritten
//coordinate: from left top corner of picture, going right x increase, going down y increase
rect(0, 400, width, 100); //draw a rectangle
//x and y of top left corner, then width and height of it
// width here means max width possible

//sun

fill(255, 255, 0);
noStroke(); //no outline for a shape drawn
ellipse(50, 50, 40, 40); //draw a circle or ellipse

//cloud

fill(255, 255, 255);
int lumps = 4;
while(lumps >0) {
  ellipse(50 + 50 * lumps, 130, 60, 60);
  ellipse(70 + 50 * lumps, 150, 60, 60); 
  // in order for cloud to be behind the tree, we need to draw cloud before I draw tree
  lumps --;
}

//tree

strokeWeight(2); //change stroke thickness
stroke(0, 200, 0); //stroke color
fill(0, 255, 0); //change fill color
ellipse(300, 250, 250, 150);
noStroke();
fill(200, 100, 0);
rect(290, 320, 20, 120);







