class ChessPiece {
	constructor(black, type, boardCTX) {
		if(black) {
			this.color = BLACK
		}

		this.boardCTX = boardCTX;
		this.type = type;

		//Temp dev code
		this.size = 2;
		var render = this.devRender.bind(this);
	}

	devRender(center) {
		this.boardCTX.beginPath();
		this.boardCTX.fillStyle = "#FF6A6A";
		this.boardCTX.arc(center.x, center.y, 0, size * Math.PI, true);
		this.boardCTX.fill();
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
		var spawnPieces = this.spawnPieces.bind(this);
		var spawnPawns = this.spawnPawns.bind(this);

		this.board.addEventListener("mousedown", ChessboardSelect);
		this.board.addEventListener("mouseup", ChessboardDeselect);

		InitializeGraphics(graphicsInfo);

		this.homePlayer = GAME.PLAYER.WHITE;
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
		for(var i = 0; i < this.rowSize; i++){
			if(i < 1 || i > 6) {
				this.boardArraythis.spawnPieces(i);
			}

			if(i == 1 || i == 6) {
				this.spawnPawns(i);
			}
		}
	}

	spawnPieces(row) {
		var isBlack = false;
		var yStart = 0;
		
		if(row == 0) {
			if(this.homePlayer == GAME.PLAYER.WHITE) {
				isBlack = true;
			}
		}

		if(row == 7) {
			if(this.homePlayer == GAME.PLAYER.BLACK) {
				isBlack = true;
				yStart = this.rowSize * 7;
			}
		}
		var rook1 = ChessPiece(isBlack, ROOK, this.boardCTX);
		var rook2 = ChessPiece(!isBlack, ROOK, this.boardCTX);
		
	}

	spawnPawns(row) {

	}

	InitializeData() {
		let defaultData = [];

	}

	ChessboardSelect(event) {
		let clickX = event.pageX % this.board.width;
		let clickY = event.pageY % this.board.height;

		let rowNumber = Math.floor(clickX / this.rowSize);
		let columnNumber = Math.floor(clickY / this.columnSize);

		this.boardCTX.fillStyle = "rgb(50,255,50)";
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
