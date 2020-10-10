class Chessboard {
	constructor(parentdiv, cpu, players, graphicsInfo) {
		this.parentdiv = parentdiv;

		this.board = document.createElement("CANVAS");
		this.boardCTX = this.board.getContext('2d');
		
		this.parentdiv.appendChild(this.board);
	
		this.InitializeGraphics(graphicsInfo);

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
			this.board.width = 800;
			this.board.height = 800;
		} else { 
			if(-('-' + graphicsInfo.width != NaN)) {
				this.board.width = graphicsInfo.width;
			} else {
				this.board.width = 800;
			}

			if(-('-' + graphicsInfo.height != NaN)) {
				this.board.height = 800;
			} else {
				this.board.height = 800
			}
		}

	}
}
