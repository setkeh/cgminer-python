"""
Web Front end to Cgminer-python
Written by: Setkeh setkeh <at> gmail <dot> com
https://github.com/setkeh
"""

# Import CherryPy global namespace
import cherrypy
import os
from scripts.cgminerversion import * 
from scripts.cgminerconfig import *
from scripts.coin import *
from scripts.pga0 import *
from scripts.pga1 import *
from scripts.pga2 import *
from scripts.pga3 import *
from scripts.pga4 import *
from scripts.pga5 import *
from scripts.pga6 import *
from scripts.pga7 import *
from scripts.pga8 import *
from scripts.pga9 import *
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))
tmpl = env.get_template('index.html')
cherrypy.config.update("main.conf")

class Root(object):

    @cherrypy.expose
    def index(self):
        return tmpl.render(
			title='CGminer Python', 
			page_title='CGminer Python - Stats',
			cgversion=cg_version(),
			apiver=api_version(),
			pgacount=pga_count(),
			asiccount=asic_count(),
			poolcount=pool_count(),
			poolstrat=pool_stratergy(),
			os=miner_os(),
			hashmeth=hash_method(),
			cbh=current_block_hash(),
			Longpoll=long_poll(),
			diff=diff(),
			pga0_hr=p0_mhs(),
			pga0_acc=p0_accepted(),
			pga0_rej=p0_rejected(),
			pga0_err=p0_hwerrors(),
			pga0_util=p0_utility(),
			pga1_hr=p1_mhs(),
			pga1_acc=p1_accepted(),
			pga1_rej=p1_rejected(),
			pga1_err=p1_hwerrors(),
			pga1_util=p1_utility(),
			pga2_hr=p2_mhs(),
			pga2_acc=p2_accepted(),
			pga2_rej=p2_rejected(),
			pga2_err=p2_hwerrors(),
			pga2_util=p2_utility(),
			pga3_hr=p3_mhs(),
			pga3_acc=p3_accepted(),
			pga3_rej=p3_rejected(),
			pga3_err=p3_hwerrors(),
			pga3_util=p3_utility(),
			pga4_hr=p4_mhs(),
			pga4_acc=p4_accepted(),
			pga4_rej=p4_rejected(),
			pga4_err=p4_hwerrors(),
			pga4_util=p4_utility(),
			pga5_hr=p5_mhs(),
			pga5_acc=p5_accepted(),
			pga5_rej=p5_rejected(),
			pga5_err=p5_hwerrors(),
			pga5_util=p5_utility(),
			pga6_hr=p6_mhs(),
			pga6_acc=p6_accepted(),
			pga6_rej=p6_rejected(),
			pga6_err=p6_hwerrors(),
			pga6_util=p6_utility(),
			pga7_hr=p7_mhs(),
			pga7_acc=p7_accepted(),
			pga7_rej=p7_rejected(),
			pga7_err=p7_hwerrors(),
			pga7_util=p7_utility(),
			pga8_hr=p8_mhs(),
			pga8_acc=p8_accepted(),
			pga8_rej=p8_rejected(),
			pga8_err=p8_hwerrors(),
			pga8_util=p8_utility(),
			pga9_hr=p9_mhs(),
			pga9_acc=p9_accepted(),
			pga9_rej=p9_rejected(),
			pga9_err=p9_hwerrors(),
			pga9_util=p9_utility(),
			)

#    @cherrypy.expos
#    def cgversion(self):
#	return tmpl.render(cgversion=cg_version())

import os.path
mainconf = os.path.join(os.path.dirname(__file__), 'main.conf')
cherrypy.tree.mount(Root(), "/", config=mainconf) 

cherrypy.engine.start()
cherrypy.engine.block()
