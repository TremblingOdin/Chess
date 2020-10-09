import Chessboard from './index/chessboard.js";

window.onload = () => {
	var players = new Object();
	players.player1 = true;
	players.player2 = true;

	const chessboard = new Chessboard("chessboard", false, players);
};
