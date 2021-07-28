
from os import path

# BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(BASE_PATH)

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import StaticFileHandler,Application
from backend.tools.get_host_ip import host_ip
from backend.webInterface import tr_run
from backend.webInterface import tr_index
from backend.tools import log
import logging
logger = logging.getLogger(log.LOGGER_ROOT_NAME+'.'+__name__)


class OCRServer:
    def __init__(self):
        self.current_path = path.dirname(__file__)
        self.settings = dict(
            # debug=True,
            static_path=path.join(self.current_path, "dist/chineseocr_lite_fontend")  # 配置静态文件路径
        )
        self.port = 8089
        self.server = HTTPServer(self.make_app())
        self.server.bind(self.port)

    def make_app(self):
        return Application([
            (r"/api/tr-run/", tr_run.TrRun),
            (r"/api/tr-run", tr_run.TrRun),
            (r"/", tr_index.Index),
            (r"/(.*)", StaticFileHandler,{"path": path.join(self.current_path, "dist/chineseocr_lite_fontend"), "default_filename": "index.html"}),
            ],
            **self.settings)


    def stop_server(self):
        self.server.stop()
        # silence StreamClosedError Tornado is throwing after it is stopped
        #log.getLogger().setLevel(log.FATAL)
        ioloop = IOLoop.current()
        ioloop.add_callback(ioloop.stop)
        print("Asked Tornado to exit")

    ##单独启用服务
    def startup(self):
        import asyncio
        asyncio.set_event_loop(asyncio.new_event_loop())
        
        self.server.start(1)
        print(f'server is running: {host_ip()}:{self.port}')
        IOLoop.current().start()

if __name__ == "__main__":
    OCRServer().startup()