import React, { useEffect, useRef } from "react";

function Canvas(props) {
	const { allPath, maze, pathResult } = props.props;
	const canvasRef = useRef(null);
	let borderWidth = Math.min(window.innerWidth, window.innerHeight);
	borderWidth = Math.max(borderWidth, 500);
	let roadWidth = borderWidth / maze[0].length;
	let roadHeight = borderWidth / maze.length;

	let reload = useRef(false)

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
		path.forEach((position) => {
			context.beginPath();
			context.rect(position.x * roadWidth, position.y * roadHeight, roadWidth, roadHeight);
			context.fillStyle = "blue";
			context.fill();
			context.closePath();
		});
		function drawDetailedPath(detailedPath, index) {
			let item = detailedPath[index];
			setTimeout(() => {
				// if()
				context.beginPath();
				context.rect(item.x * roadWidth, item.y * roadWidth, roadWidth, roadWidth);
				context.fillStyle = "red";
				context.fill();
				context.closePath();

				if (index + 1 < detailedPath.length) drawDetailedPath(detailedPath, index + 1);
			}, 20);
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
	},);

	// useEffect(() => {
	// 	const controller = new AbortController();
	// 	startLoad(controller.signal);
	// 	return () => {
	// 		controller.abort();
	// 	};
		
	// },);

	// const startLoad = async (signal) => {
	// 	const canvas = canvasRef.current;
	// 	if (signal.aborted) {
	// 		return;
	// 	}
	// 	const context = canvas.getContext("2d");
	// 	if (signal.aborted) {
	// 		return;
	// 	}
	// 	renderMaze2(canvas, context, maze);
	// 	if (signal.aborted) {
	// 		return;
	// 	}
	// 	await renderPath(canvas, context);
	// 	if (signal.aborted) {
	// 		return;
	// 	}
	// };

	return <canvas ref={canvasRef} {...props} height="600px" width="600px" />;
}
export default Canvas;
