pygmentize := pygmentize

all:
	$(pygmentize) -l dg -o index.websocket.html index.websocket.dg
	$(pygmentize) -l dg -o index.hello-world.html index.hello-world.dg
	$(pygmentize) -l bash -o index.wrk.html index.wrk.sh
