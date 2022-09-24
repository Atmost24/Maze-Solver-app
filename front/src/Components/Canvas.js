import React, { useEffect, useRef } from "react";
import { mazeArray } from "../maze_files/mazeArray51";
import { MazeSolver } from "../Class/MazeSolver1";

//PASAR MAZEARRAY COMO PROP
function Canvas(props) {
	const canvasRef = useRef(null);
	let borderWidth = Math.min(window.innerWidth, window.innerHeight);
	borderWidth = Math.max(borderWidth, 500);
	let roadWidth = borderWidth / mazeArray[0].length;
	let roadHeight = borderWidth / mazeArray.length;

	const renderMaze2 = (canvas, context, mazeArray) => {
		canvas.width = borderWidth;
		canvas.height = borderWidth;
		for (let i = 0; i < mazeArray.length; i++) {
			for (let j = 0; j < mazeArray[i].length; j++) {
				context.beginPath();

				context.rect(j * roadWidth, i * roadHeight, roadWidth, roadHeight);

				context.fillStyle = mazeArray[i][j] === 0 ? "white" : "black";
				context.fill();

				context.closePath();
			}
		}
	};

	const renderPath = (canvas, context) => {
		let mazeSolver = new MazeSolver(mazeArray);
		let path = mazeSolver.solveMaze();
		console.log(">>path:", path);
		path.forEach((position) => {
			context.beginPath();

			context.rect(position.x * roadWidth, position.y * roadHeight, roadWidth, roadHeight);

			context.fillStyle = "blue";
			context.fill();

			context.closePath();
		});

    function drawDetailedPath (detailedPath, index) {
      let item = detailedPath[index]
      setTimeout(() => {
        context.beginPath()
        context.rect(item.position.x * roadWidth, item.position.y * roadWidth, roadWidth, roadWidth)
        context.fillStyle = item.type === 'enter' ? 'red' : 'white'
        context.fill()
        context.closePath()
  
        if (index + 1 < detailedPath.length)
          drawDetailedPath(detailedPath, index + 1)
      }, 20)
    }
    drawDetailedPath(mazeSolver.detailedPath, 0)
	};

  


	useEffect(() => {
		const canvas = canvasRef.current;
		const context = canvas.getContext("2d");
		// renderMaze(context, mazeArray_);
		renderMaze2(canvas, context, mazeArray);
		renderPath(canvas, context);
	}, [renderMaze2]);

	return <canvas ref={canvasRef} {...props} height="600px" width="600px" />;
}
export default Canvas;
