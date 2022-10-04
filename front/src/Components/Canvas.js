import React, { useEffect, useRef } from "react";

function Canvas(props) {
	const { allPath, maze, pathResult } = props.props;
	let length = maze.length
	let timeOut = 0;
	if ( length <= 10) timeOut = 200
	else if (length <= 50) timeOut = 25
	else if (length <= 100) timeOut = 10
	else if (length <= 200) timeOut = 5
	else timeOut = 1
	const canvasRef = useRef(null);
	let borderWidth = Math.min(window.innerWidth, window.innerHeight);
	borderWidth = Math.max(borderWidth, 500);
	let roadWidth = borderWidth / maze[0].length;
	let roadHeight = borderWidth / maze.length;

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
		let path = pathResult;
		drawDetailedPath(allPath, 0);
		
		function drawDetailedPath(detailedPath, index) {
			let item = detailedPath[index];
			setTimeout(() => {
				context.beginPath();
				context.rect(item.x * roadWidth, item.y * roadWidth, roadWidth, roadWidth);
				if (path.some((e) => e.x === detailedPath[index].x && e.y === detailedPath[index].y)) {
					context.fillStyle = "#08D9D6";
				} else context.fillStyle = "#FF2E63";
				context.fill();
				context.closePath();
				if (index + 1 < detailedPath.length) drawDetailedPath(detailedPath, index + 1);
			}, timeOut);
		}
	};

	//https://stackoverflow.com/questions/69618671/stop-executing-function-after-data-change-react-useeffect
	//stop the execution of a function from a useeffect
	//https://stackoverflow.com/questions/68486331/how-to-stop-a-useeffect-function-with-a-condition
	//probar haciendo un lock toca esperar hasta que termnine para hacer cambios
	useEffect(() => {
		const canvas = canvasRef.current;
		const context = canvas.getContext("2d");
		renderMaze2(canvas, context, maze);
		renderPath(canvas, context);
	});

	return (
		<div>
			<h4>Solucion</h4>
			<canvas ref={canvasRef} {...props} height="600px" width="600px" />
		</div>
	);
}
export default Canvas;
