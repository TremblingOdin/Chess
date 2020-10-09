class Chessboard {
	constructor(parentdiv, cpu, players) {
		this.parentdiv = parentdiv;
		this.board = document.createElement("CANVAS");
		this.boardCTX = this.board.getContext('2d');
		
		/*
		if(cpu != false) {
			this.player2 = cpu;
			this.player1 = players.player1;
		} else {
			this.player1 = players.player1;
			this.player2 = players.player2;
		}*/
	}
}
