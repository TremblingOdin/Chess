window.onload = () => {
	var players = new Object();
	players.player1 = true;
	players.player2 = true;

	var graphicsInfo = null;

	const chessboard = new Chessboard(document.getElementById("chessboard"), false, players, graphicsInfo);
}
