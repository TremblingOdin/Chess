class Chessboard {
	constructor(elementid, cpu, players) {
		document.getElementById(elementid);
		if(cpu != false) {
			this.player2 = cpu;
			this.player1 = players.player1;
		} else {
			this.player1 = players.player1;
			this.player2 = players.player2;
		}
	}
}

export { Chessboard };
