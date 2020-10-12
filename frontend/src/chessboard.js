function defineEnumProperty(ctx) {
	return (prop, value) => {
		Object.defineProperty(ctx, prop, {
			configurable: false,
			writable: false,
			enumerable: true,
			value: value
		});
	}
}

function Color() {
	return Color;
}

Color.values = function() {
	return Object.keys(Color)
		.filter(key => typeof Color[key] !== 'function')
		.sort((key1, key2) => Color[key1] - Color[key2]);
}

Color.keys = function() {
	return Color.values()
		.map(key => Color[key]);
}

Color.getByValue = function(val) {
	return Color.values()
		.find(colorValue => Color[colorValue] === val);
}

var addEnumValue = defineEnumProperty(Color), colors = ['WHITE', 'BLACK'];
colors.forEach((color, index) => {
	addEnumValue(color, index);
});

class ChessPiece {
	constructor(black, type) {
		if(black) {
			this.color = BLACK;
		}
	}
}

class Chessboard {
	constructor(parentdiv, cpu, players, graphicsInfo) {
		this.parentdiv = parentdiv;

		this.board = document.createElement("CANVAS");
		this.boardCTX = this.board.getContext('2d');
		
		this.parentdiv.appendChild(this.board);

		var ChessboardSelect = this.ChessboardSelect.bind(this);
		var ChessboardDeselect = this.ChessboardDeselect.bind(this);
		var InitializeData = this.InitializeData.bind(this);
		var InitializeGraphics = this.InitializeGraphics.bind(this);

		this.board.addEventListener("mousedown", ChessboardSelect);
		this.board.addEventListener("mouseup", ChessboardDeselect);

		InitializeGraphics(graphicsInfo);
		this.boardArray = InitializeData();

		/*
		if(cpu != false) {
			this.player2 = cpu;
			this.player1 = players.player1;
		} else {
			this.player1 = players.player1;
			this.player2 = players.player2;
		}*/
	}

	InitializeGraphics(graphicsInfo) {
		if(graphicsInfo == null || graphicsInfo == undefined) {
			this.board.width = 500;
			this.board.height = 500;
		} else { 
			if(-('-' + graphicsInfo.width != NaN)) {
				this.board.width = graphicsInfo.width;
			} else {
				this.board.width = 500;
			}

			if(-('-' + graphicsInfo.height != NaN)) {
				this.board.height = 500;
			} else {
				this.board.height = 500
			}
		}
		
		let rowCount = 8;
		let columnCount = 8;

		this.rowSize = this.board.height / 8;
		this.columnSize = this.board.width / 8;

		let rowStartBlack = true;
		//On my chessboard at home, sometimes a row will end on black then then next one will start on black so I dunno this is how I'm fixing that
		for(var i = 0; i < rowCount; i++) {
			let isBlack = rowStartBlack;
			for(var j = 0; j < columnCount; j++) {
				if(isBlack) {
					this.boardCTX.fillStyle = "rgb(255,255,255)";
					this.boardCTX.fillRect(i * this.rowSize, j * this.columnSize, 
						this.rowSize, this.columnSize);
				} else {
					this.boardCTX.fillStyle = "rgb(22,22,22)";
					this.boardCTX.fillRect(i * this.rowSize, j * this.columnSize, 
						this.rowSize, this.columnSize);
				}

				isBlack = !isBlack;
			}

			rowStartBlack = !rowStartBlack;
		}

		//TODO: MAke icons and load in icons
	}

	InitializeData() {
		let defaultData = [];

	}

	ChessboardSelect(event) {
		let clickX = event.pageX % this.board.width;
		let clickY = event.pageY % this.board.height;

		let rowNumber = Math.floor(clickX / this.rowSize);
		let columnNumber = Math.floor(clickY / this.columnSize);

		this.boardCTX.fillStyle = "rgba(50,255,50,0.5)";
		this.boardCTX.fillRect(rowNumber * this.rowSize, columnNumber * this.columnSize, 
			this.rowSize, this.columnSize);
	}

	ChessboardDeselect(event) {
		let clickX = event.pageX % this.board.width;
		let clickY = event.pageY % this.board.height;

		let rowNumber = Math.floor(clickX / this.rowSize);
		let columnNumber = Math.floor(clickY/ this.columnSize);

		//If the row is even, all even columns are white and odd are black
		//If the row is odd, all even columns are black and odd are white
		if(rowNumber % 2 == 0) {
			if(columnNumber % 2 == 1) {
				this.boardCTX.fillStyle = "rgb(22,22,22)";
			} else {
				this.boardCTX.fillStyle = "rgb(255,255,255)";
			}
		} else {
			if(columnNumber % 2 == 1) {
				this.boardCTX.fillStyle = "rgb(255,255,255)";
			} else {
				this.boardCTX.fillStyle = "rgb(22,22,22)";
			}
		}
		
		this.boardCTX.fillRect(rowNumber * this.rowSize, columnNumber * this.columnSize,
			this.rowSize, this.columnSize);
	}
}
