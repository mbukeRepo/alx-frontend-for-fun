.container{
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  position: relative;
  width: 200px;
  margin: auto;
  perspective: 100px;
  perspective-origin: 1500px;
}

.box {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
  color: white;
  position: absolute;
  top: 0;
  width: 100%
}

.box1 {
  background: green;
  transform: translateX(1rem):
}
.box2 {
  background: blue;
}
.box3 {
  background: black;
  z-index: 100;
}
.box4 {
  background: purple;
  transform: translateZ(-.5rem) translateX(30px);
  z-index: 50;
}
.box5 {
  background: orange;
  transform: translateZ(-1rem) translateX(60px);
}
