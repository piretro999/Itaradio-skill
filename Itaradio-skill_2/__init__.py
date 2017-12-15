from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
try:
    from mycroft.skills.audioservice import AudioService
except:
    from mycroft.util import play_mp3
    AudioService = None
from bs4 import BeautifulSoup
import requests


__author__ = 'mmeyer'

LOGGER = getLogger(__name__)


Discoradio_URL = 'http://46.37.20.206:1935/live/1discoradio.stream/playlist.m3u8'
LifeGateRadio_URL = 'http://onair11.xdevel.com:8024'
R101Diretta_URL = 'http://icecast.unitedradio.it/r101'
Radio105_URL = 'http://icecast.105.net/105.mp3'
Radio24_URL = 'http://shoutcast.radio24.it:8000/listen.pls'
RadioAmoreCampania_URL = 'http://onair11.xdevel.com:8002'
RadioCapital_URL = 'http://radiocapital-lh.akamaihd.net/i/RadioCapital_Live_1@196312/master.m3u8'
RadioCuore_URL = 'http://nr9.newradio.it:9029'
RadioDeejay_URL = 'http://radiodeejay-lh.akamaihd.net/i/RadioDeejay_Live_1@189857/master.m3u8'
RadioIbiza_URL = 'http://wma02.fluidstream.net:5010/'
RadioKissKissItalia_URL = 'http://wma07.fluidstream.net:3616/;stream.nsv'
RadioKissKissNapoli_URL = 'http://ice08.fluidstream.net/KKNapoli.aac'
RadioKissKiss_URL = 'http://ice07.fluidstream.net:8080/KissKiss.mp3'
RadioLatteMiele_URL = 'http://onair18.xdevel.com:8014/'
Radiom2o_URL = 'http://radiom2o-lh.akamaihd.net/i/RadioM2o_Live_1@42518/master.m3u8'
RadioMarte_URL = 'http://onair18.xdevel.com:8212/'
RadioPlaystudio_URL = 'http://playstudio.serverroom.us:4140'
RadioRCSlOndaVeronese_URL = 'http://176.31.254.217:8030/'
RadioSportiva_URL = 'http://nr5.newradio.it:8545/stream.mp3'
RadioStudioDelta_URL = 'http://5.63.145.172:7203/'
RadioSubasio_URL = 'http://onair18.xdevel.com:8152'
RadioZetaLItaliana_URL = 'http://shoutcast.rtl.it:3030/stream/1/'
RadionorbaMusicSport_URL = 'http://onair7.xdevel.com:8738/'
Radionorba_URL = 'http://onair11.xdevel.com:9990/'
RaiGrParlamento_URL = 'http://icestreaming.rai.it/7.mp3'
RaiIsoRadio_URL = 'http://icestreaming.rai.it/6.mp3'
RaiRadio1_URL = 'http://icestreaming.rai.it/1.mp3'
RaiRadio2_URL = 'http://icestreaming.rai.it/2.mp3'
RaiRadio3_URL = 'http://icestreaming.rai.it/3.mp3'
RaiRadio4Light_URL = 'http://icestreaming.rai.it/4.mp3'
RaiRadio5Classica_URL = 'http://icestreaming.rai.it/5.mp3'
RaiRadio6Teca_URL = 'http://icestreaming.rai.it:80/9.mp3'
RaiRadio7Live_URL = 'http://icestreaming.rai.it:80/10.mp3'
RaiRadio8Opera_URL = 'http://icestreaming.rai.it:80/11.mp3'
RamPower1027_URL = 'http://46.37.20.206:1935/live/1ram.stream/playlist.m3u8'
RDS_URL = 'http://www.rds.it:8000/stream'
RINRadioItaliaNetwork_URL = 'http://sr9.inmystream.info:8006'
RMCRadioMonteCarlo_URL = 'http://edge.radiomontecarlo.net/RMC.mp3'
RMC2RadioMonteCarlo2_URL = 'http://edge.radiomontecarlo.net/MC2.mp3'
RTLBest_URL = 'http://shoutcast.rtl.it:3020/'
RTLGroove_URL = 'http://shoutcast.rtl.it:3040/'
RTLItalianStyle_URL = 'http://shoutcast.rtl.it:3030/'
RTLLounge_URL = 'http://shoutcast.rtl.it:3070/'
RTLRadiofreccia_URL = 'http://shoutcast.rtl.it:3060/'
RTL_URL = 'http://shoutcast.rtl.it:3010/'
StudioradioTheVintageStation_URL = 'http://91.121.38.216:8060/'
VirginRadio_URL = 'http://icecast.unitedradio.it/Virgin.mp3'


class ItaradioSkill(MycroftSkill):
    def __init__(self):
        super(ItaradioSkill, self).__init__(name="ItaradioSkill")
        self.audioservice = None

    def initialize(self):
        if AudioService:
            self.audioservice = AudioService(self.emitter)

						 
        whatson_Discoradio_intent = IntentBuilder("WhatsonDlfIntent").\
                         require("WhatsonKeyword").\
                         require("DiscoradioKeyword").build()
        self.register_intent(whatson_Discoradio_intent, self.handle_whatson_Discoradio_intent)
        whatson_LifeGateRadio_intent = IntentBuilder("WhatsonLifeGateRadioIntent").\
                         require("WhatsonKeyword").\
                         require("LifeGateRadioKeyword").build()
        self.register_intent(whatson_LifeGateRadio_intent, self.handle_whatson_LifeGateRadio_intent)
        whatson_R101Diretta_intent = IntentBuilder("WhatsonR101DirettaIntent").\
                         require("WhatsonKeyword").\
                         require("R101DirettaKeyword").build()
        self.register_intent(whatson_R101Diretta_intent, self.handle_whatson_R101Diretta_intent)
        whatson_Radio105_intent = IntentBuilder("WhatsonRadio105Intent").\
                         require("WhatsonKeyword").\
                         require("Radio105Keyword").build()
        self.register_intent(whatson_Radio105_intent, self.handle_whatson_Radio105_intent)
        whatson_Radio24_intent = IntentBuilder("WhatsonRadio24Intent").\
                         require("WhatsonKeyword").\
                         require("Radio24Keyword").build()
        self.register_intent(whatson_Radio24_intent, self.handle_whatson_Radio24_intent)
        whatson_RadioAmoreCampania_intent = IntentBuilder("WhatsonRadioAmoreCampaniaIntent").\
                         require("WhatsonKeyword").\
                         require("RadioAmoreCampaniaKeyword").build()
        self.register_intent(whatson_RadioAmoreCampania_intent, self.handle_whatson_RadioAmoreCampania_intent)
        whatson_RadioCapital_intent = IntentBuilder("WhatsonRadioCapitalIntent").\
                         require("WhatsonKeyword").\
                         require("RadioCapitalKeyword").build()
        self.register_intent(whatson_RadioCapital_intent, self.handle_whatson_RadioCapital_intent)
        whatson_RadioCuore_intent = IntentBuilder("WhatsonRadioCuoreIntent").\
                         require("WhatsonKeyword").\
                         require("RadioCuoreKeyword").build()
        self.register_intent(whatson_RadioCuore_intent, self.handle_whatson_RadioCuore_intent)
        whatson_RadioDeejay_intent = IntentBuilder("WhatsonRadioDeejayIntent").\
                         require("WhatsonKeyword").\
                         require("RadioDeejayKeyword").build()
        self.register_intent(whatson_RadioDeejay_intent, self.handle_whatson_RadioDeejay_intent)
        whatson_RadioIbiza_intent = IntentBuilder("WhatsonRadioIbizaIntent").\
                         require("WhatsonKeyword").\
                         require("RadioIbizaKeyword").build()
        self.register_intent(whatson_RadioIbiza_intent, self.handle_whatson_RadioIbiza_intent)
        whatson_RadioKissKissItalia_intent = IntentBuilder("WhatsonRadioKissKissItaliaIntent").\
                         require("WhatsonKeyword").\
                         require("RadioKissKissItaliaKeyword").build()
        self.register_intent(whatson_RadioKissKissItalia_intent, self.handle_whatson_RadioKissKissItalia_intent)
        whatson_RadioKissKissNapoli_intent = IntentBuilder("WhatsonRadioKissKissNapoliIntent").\
                         require("WhatsonKeyword").\
                         require("RadioKissKissNapoliKeyword").build()
        self.register_intent(whatson_RadioKissKissNapoli_intent, self.handle_whatson_RadioKissKissNapoli_intent)
        whatson_RadioKissKiss_intent = IntentBuilder("WhatsonRadioKissKissIntent").\
                         require("WhatsonKeyword").\
                         require("RadioKissKissKeyword").build()
        self.register_intent(whatson_RadioKissKiss_intent, self.handle_whatson_RadioKissKiss_intent)
        whatson_RadioLatteMiele_intent = IntentBuilder("WhatsonRadioLatteMieleIntent").\
                         require("WhatsonKeyword").\
                         require("RadioLatteMieleKeyword").build()
        self.register_intent(whatson_RadioLatteMiele_intent, self.handle_whatson_RadioLatteMiele_intent)
        whatson_Radiom2o_intent = IntentBuilder("WhatsonRadiom2oIntent").\
                         require("WhatsonKeyword").\
                         require("Radiom2oKeyword").build()
        self.register_intent(whatson_Radiom2o_intent, self.handle_whatson_Radiom2o_intent)
        whatson_RadioMarte_intent = IntentBuilder("WhatsonRadioMarteIntent").\
                         require("WhatsonKeyword").\
                         require("RadioMarteKeyword").build()
        self.register_intent(whatson_RadioMarte_intent, self.handle_whatson_RadioMarte_intent)
        whatson_RadioPlaystudio_intent = IntentBuilder("WhatsonRadioPlaystudioIntent").\
                         require("WhatsonKeyword").\
                         require("RadioPlaystudioKeyword").build()
        self.register_intent(whatson_RadioPlaystudio_intent, self.handle_whatson_RadioPlaystudio_intent)
        whatson_RadioRCSl’OndaVeronese_intent = IntentBuilder("WhatsonRadioRCSlOndaVeroneseIntent").\
                         require("WhatsonKeyword").\
                         require("RadioRCSlOndaVeroneseKeyword").build()
        self.register_intent(whatson_RadioRCSl’OndaVeronese_intent, self.handle_whatson_RadioRCSl’OndaVeronese_intent)
        whatson_RadioSportiva_intent = IntentBuilder("WhatsonRadioSportivaIntent").\
                         require("WhatsonKeyword").\
                         require("RadioSportivaKeyword").build()
        self.register_intent(whatson_RadioSportiva_intent, self.handle_whatson_RadioSportiva_intent)
        whatson_RadioStudioDelta_intent = IntentBuilder("WhatsonRadioStudioDeltaIntent").\
                         require("WhatsonKeyword").\
                         require("RadioStudioDeltaKeyword").build()
        self.register_intent(whatson_RadioSubasio+_intent, self.handle_whatson_RadioSubasio+_intent)
        whatson_RadioSubasio_intent = IntentBuilder("WhatsonRadioSubasioIntent").\
                         require("WhatsonKeyword").\
                         require("RadioSubasioKeyword").build()
        self.register_intent(whatson_RadioSubasio_intent, self.handle_whatson_RadioSubasio_intent)
        whatson_RadioZetalItaliana_intent = IntentBuilder("WhatsonRadioZetalItalianaIntent").\
                         require("WhatsonKeyword").\
                         require("RadioZetalItalianaKeyword").build()
        self.register_intent(whatson_RadioZetalItaliana_intent, self.handle_whatson_RadioZetalItaliana_intent)
        whatson_RadionorbaMusicSport_intent = IntentBuilder("WhatsonRadionorbaMusicSportIntent").\
                         require("WhatsonKeyword").\
                         require("RadionorbaMusicSportKeyword").build()
        self.register_intent(whatson_RadionorbaMusicSport_intent, self.handle_whatson_RadionorbaMusicSport_intent)
        whatson_Radionorba_intent = IntentBuilder("WhatsonRadionorbaIntent").\
                         require("WhatsonKeyword").\
                         require("RadionorbaKeyword").build()
        self.register_intent(whatson_Radionorba_intent, self.handle_whatson_Radionorba_intent)
        whatson_RaiGrParlamento_intent = IntentBuilder("WhatsonRaiGrParlamentoIntent").\
                         require("WhatsonKeyword").\
                         require("RaiGrParlamentoKeyword").build()
        self.register_intent(whatson_RaiGrParlamento_intent, self.handle_whatson_RaiGrParlamento_intent)
        whatson_RaiIsoRadio_intent = IntentBuilder("WhatsonRaiIsoRadioIntent").\
                         require("WhatsonKeyword").\
                         require("RaiIsoRadioKeyword").build()
        self.register_intent(whatson_RaiIsoRadio_intent, self.handle_whatson_RaiIsoRadio_intent)
        whatson_RaiRadio1_intent = IntentBuilder("WhatsonRaiRadio1Intent").\
                         require("WhatsonKeyword").\
                         require("RaiRadio1Keyword").build()
        self.register_intent(whatson_RaiRadio1_intent, self.handle_whatson_RaiRadio1_intent)
        whatson_RaiRadio2_intent = IntentBuilder("WhatsonRaiRadio2Intent").\
                         require("WhatsonKeyword").\
                         require("RaiRadio2Keyword").build()
        self.register_intent(whatson_RaiRadio2_intent, self.handle_whatson_RaiRadio2_intent)
        whatson_RaiRadio3_intent = IntentBuilder("WhatsonRaiRadio3Intent").\
                         require("WhatsonKeyword").\
                         require("RaiRadio3Keyword").build()
        self.register_intent(whatson_RaiRadio3_intent, self.handle_whatson_RaiRadio3_intent)
        whatson_RaiRadio4Light_intent = IntentBuilder("WhatsonRaiRadio4LightIntent").\
                         require("WhatsonKeyword").\
                         require("RaiRadio4LightKeyword").build()
        self.register_intent(whatson_RaiRadio4Light_intent, self.handle_whatson_RaiRadio4Light_intent)
        whatson_RaiRadio5Classica_intent = IntentBuilder("WhatsonRaiRadio5ClassicaIntent").\
                         require("WhatsonKeyword").\
                         require("RaiRadio5ClassicaKeyword").build()
        self.register_intent(whatson_RaiRadio5Classica_intent, self.handle_whatson_RaiRadio5Classica_intent)
        whatson_RaiRadio6Teca_intent = IntentBuilder("WhatsonRaiRadio6TecaIntent").\
                         require("WhatsonKeyword").\
                         require("RaiRadio6TecaKeyword").build()
        self.register_intent(whatson_RaiRadio6Teca_intent, self.handle_whatson_RaiRadio6Teca_intent)
        whatson_RaiRadio7Live_intent = IntentBuilder("WhatsonRaiRadio7LiveIntent").\
                         require("WhatsonKeyword").\
                         require("RaiRadio7LiveKeyword").build()
        self.register_intent(whatson_RaiRadio7Live_intent, self.handle_whatson_RaiRadio7Live_intent)
        whatson_RaiRadio8Opera_intent = IntentBuilder("WhatsonRaiRadio8OperaIntent").\
                         require("WhatsonKeyword").\
                         require("RaiRadio8OperaKeyword").build()
        self.register_intent(whatson_RaiRadio8Opera_intent, self.handle_whatson_RaiRadio8Opera_intent)
        whatson_RamPower1027_intent = IntentBuilder("WhatsonRamPower1027Intent").\
                         require("WhatsonKeyword").\
                         require("RamPower1027Keyword").build()
        self.register_intent(whatson_RamPower1027_intent, self.handle_whatson_RamPower1027_intent)
        whatson_RDS_intent = IntentBuilder("WhatsonRDSIntent").\
                         require("WhatsonKeyword").\
                         require("RDSKeyword").build()
        self.register_intent(whatson_RDS_intent, self.handle_whatson_RDS_intent)
        whatson_RINRadioItaliaNetwork_intent = IntentBuilder("WhatsonRINRadioItaliaNetworkIntent").\
                         require("WhatsonKeyword").\
                         require("RINRadioItaliaNetworkKeyword").build()
        self.register_intent(whatson_RINRadioItaliaNetwork_intent, self.handle_whatson_RINRadioItaliaNetwork_intent)
        whatson_RMCRadioMonteCarlo_intent = IntentBuilder("WhatsonRMCRadioMonteCarloIntent").\
                         require("WhatsonKeyword").\
                         require("RMCRadioMonteCarloKeyword").build()
        self.register_intent(whatson_RMCRadioMonteCarlo_intent, self.handle_whatson_RMCRadioMonteCarlo_intent)
        whatson_RMC2RadioMonteCarlo2_intent = IntentBuilder("WhatsonRMC2RadioMonteCarlo2Intent").\
                         require("WhatsonKeyword").\
                         require("RMC2RadioMonteCarlo2Keyword").build()
        self.register_intent(whatson_RMC2RadioMonteCarlo2_intent, self.handle_whatson_RMC2RadioMonteCarlo2_intent)
        whatson_RTLBest_intent = IntentBuilder("WhatsonRTLBestIntent").\
                         require("WhatsonKeyword").\
                         require("RTLBestKeyword").build()
        self.register_intent(whatson_RTLBest_intent, self.handle_whatson_RTLBest_intent)
        whatson_RTLGroove_intent = IntentBuilder("WhatsonRTLGrooveIntent").\
                         require("WhatsonKeyword").\
                         require("RTLGrooveKeyword").build()
        self.register_intent(whatson_RTLGroove_intent, self.handle_whatson_RTLGroove_intent)
        whatson_RTLItalianStyle_intent = IntentBuilder("WhatsonRTLItalianStyleIntent").\
                         require("WhatsonKeyword").\
                         require("RTLItalianStyleKeyword").build()
        self.register_intent(whatson_RTLItalianStyle_intent, self.handle_whatson_RTLItalianStyle_intent)
        whatson_RTLLounge_intent = IntentBuilder("WhatsonRTLLoungeIntent").\
                         require("WhatsonKeyword").\
                         require("RTLLoungeKeyword").build()
        self.register_intent(whatson_RTLLounge_intent, self.handle_whatson_RTLLounge_intent)
        whatson_RTLRadiofreccia_intent = IntentBuilder("WhatsonRTLRadiofrecciaIntent").\
                         require("WhatsonKeyword").\
                         require("RTLRadiofrecciaKeyword").build()
        self.register_intent(whatson_RTLRadiofreccia_intent, self.handle_whatson_RTLRadiofreccia_intent)
        whatson_RTL_intent = IntentBuilder("WhatsonRTLIntent").\
                         require("WhatsonKeyword").\
                         require("RTLKeyword").build()
        self.register_intent(whatson_RTL_intent, self.handle_whatson_RTL_intent)
        whatson_Studioradio–TheVintageStation_intent = IntentBuilder("WhatsonStudioradioTheVintageStationIntent").\
                         require("WhatsonKeyword").\
                         require("StudioradioTheVintageStationKeyword").build()
        self.register_intent(whatson_Studioradio–TheVintageStation_intent, self.handle_whatson_Studioradio–TheVintageStation_intent)
        whatson_VirginRadio_intent = IntentBuilder("WhatsonVirginRadioIntent").\
                         require("WhatsonKeyword").\
                         require("VirginRadioKeyword").build()
        self.register_intent(whatson_VirginRadio_intent, self.handle_whatson_VirginRadio_intent)
							 
							 
        Discoradio_intent = IntentBuilder("DiscoradioIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(Discoradio_intent, self.handle_Discoradio_intent)
        LifeGateRadio_intent = IntentBuilder("LifeGateRadioIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(LifeGateRadio_intent, self.handle_LifeGateRadio_intent)
        R101Diretta_intent = IntentBuilder("R101DirettaIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(R101Diretta_intent, self.handle_R101Diretta_intent)
        Radio105_intent = IntentBuilder("Radio105Intent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(Radio105_intent, self.handle_Radio105_intent)
        Radio24_intent = IntentBuilder("Radio24Intent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(Radio24_intent, self.handle_Radio24_intent)
        RadioAmoreCampania_intent = IntentBuilder("RadioAmoreCampaniaIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RadioAmoreCampania_intent, self.handle_RadioAmoreCampania_intent)
        RadioCapital_intent = IntentBuilder("RadioCapitalIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RadioCapital_intent, self.handle_RadioCapital_intent)
        RadioCuore_intent = IntentBuilder("RadioCuoreIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RadioCuore_intent, self.handle_RadioCuore_intent)
        RadioDeejay_intent = IntentBuilder("RadioDeejayIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RadioDeejay_intent, self.handle_RadioDeejay_intent)
        RadioIbiza_intent = IntentBuilder("RadioIbizaIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RadioIbiza_intent, self.handle_RadioIbiza_intent)
        RadioKissKissItalia_intent = IntentBuilder("RadioKissKissItaliaIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RadioKissKissItalia_intent, self.handle_RadioKissKissItalia_intent)
        RadioKissKissNapoli_intent = IntentBuilder("RadioKissKissNapoliIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RadioKissKissNapoli_intent, self.handle_RadioKissKissNapoli_intent)
        RadioKissKiss_intent = IntentBuilder("RadioKissKissIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RadioKissKiss_intent, self.handle_RadioKissKiss_intent)
        RadioLatteMiele_intent = IntentBuilder("RadioLatteMieleIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RadioLatteMiele_intent, self.handle_RadioLatteMiele_intent)
        Radiom2o_intent = IntentBuilder("Radiom2oIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(Radiom2o_intent, self.handle_Radiom2o_intent)
        RadioMarte_intent = IntentBuilder("RadioMarteIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RadioMarte_intent, self.handle_RadioMarte_intent)
        RadioPlaystudio_intent = IntentBuilder("RadioPlaystudioIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RadioPlaystudio_intent, self.handle_RadioPlaystudio_intent)
        RadioRCSlOndaVeronese_intent = IntentBuilder("RadioRCSlOndaVeroneseIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RadioRCSlOndaVeronese_intent, self.handle_RadioRCSlOndaVeronese_intent)
        RadioSportiva_intent = IntentBuilder("RadioSportivaIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RadioSportiva_intent, self.handle_RadioSportiva_intent)
        RadioStudioDelta_intent = IntentBuilder("RadioStudioDeltaIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RadioStudioDelta_intent, self.handle_RadioStudioDelta_intent)
        RadioSubasio_intent = IntentBuilder("RadioSubasioIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RadioSubasio_intent, self.handle_RadioSubasio_intent)
        RadioZetalItaliana_intent = IntentBuilder("RadioZetalItalianaIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RadioZetalItaliana_intent, self.handle_RadioZetalItaliana_intent)
        RadionorbaMusicSport_intent = IntentBuilder("RadionorbaMusicSportIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RadionorbaMusicSport_intent, self.handle_RadionorbaMusicSport_intent)
        Radionorba_intent = IntentBuilder("RadionorbaIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(Radionorba_intent, self.handle_Radionorba_intent)
        RaiGrParlamento_intent = IntentBuilder("RaiGrParlamentoIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RaiGrParlamento_intent, self.handle_RaiGrParlamento_intent)
        RaiIsoRadio_intent = IntentBuilder("RaiIsoRadioIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RaiIsoRadio_intent, self.handle_RaiIsoRadio_intent)
        RaiRadio1_intent = IntentBuilder("RaiRadio1Intent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RaiRadio1_intent, self.handle_RaiRadio1_intent)
        RaiRadio2_intent = IntentBuilder("RaiRadio2Intent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RaiRadio2_intent, self.handle_RaiRadio2_intent)
        RaiRadio3_intent = IntentBuilder("RaiRadio3Intent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RaiRadio3_intent, self.handle_RaiRadio3_intent)
        RaiRadio4Light_intent = IntentBuilder("RaiRadio4LightIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RaiRadio4Light_intent, self.handle_RaiRadio4Light_intent)
        RaiRadio5Classica_intent = IntentBuilder("RaiRadio5ClassicaIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RaiRadio5Classica_intent, self.handle_RaiRadio5Classica_intent)
        RaiRadio6Teca_intent = IntentBuilder("RaiRadio6TecaIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RaiRadio6Teca_intent, self.handle_RaiRadio6Teca_intent)
        RaiRadio7Live_intent = IntentBuilder("RaiRadio7LiveIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RaiRadio7Live_intent, self.handle_RaiRadio7Live_intent)
        RaiRadio8Opera_intent = IntentBuilder("RaiRadio8OperaIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RaiRadio8Opera_intent, self.handle_RaiRadio8Opera_intent)
        RamPower1027_intent = IntentBuilder("RamPower1027Intent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RamPower1027_intent, self.handle_RamPower1027_intent)
        RDS_intent = IntentBuilder("RDSIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RDS_intent, self.handle_RDS_intent)
        RINRadioItaliaNetwork_intent = IntentBuilder("RINRadioItaliaNetworkIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RINRadioItaliaNetwork_intent, self.handle_RINRadioItaliaNetwork_intent)
        RMCRadioMonteCarlo_intent = IntentBuilder("RMCRadioMonteCarloIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RMCRadioMonteCarlo_intent, self.handle_RMCRadioMonteCarlo_intent)
        RMC2RadioMonteCarlo2_intent = IntentBuilder("RMC2RadioMonteCarlo2Intent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RMC2RadioMonteCarlo2_intent, self.handle_RMC2RadioMonteCarlo2_intent)
        RTLBest_intent = IntentBuilder("RTLBestIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RTLBest_intent, self.handle_RTLBest_intent)
        RTLGroove_intent = IntentBuilder("RTLGrooveIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RTLGroove_intent, self.handle_RTLGroove_intent)
        RTLItalianStyle_intent = IntentBuilder("RTLItalianStyleIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RTLItalianStyle_intent, self.handle_RTLItalianStyle_intent)
        RTLLounge_intent = IntentBuilder("RTLLoungeIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RTLLounge_intent, self.handle_RTLLounge_intent)
        RTLRadiofreccia_intent = IntentBuilder("RTLRadiofrecciaIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RTLRadiofreccia_intent, self.handle_RTLRadiofreccia_intent)
        RTL_intent = IntentBuilder("RTLIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(RTL_intent, self.handle_RTL_intent)
        StudioradioTheVintageStation_intent = IntentBuilder("StudioradioTheVintageStationIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(StudioradioTheVintageStation_intent, self.handle_StudioradioTheVintageStation_intent)
        VirginRadio_intent = IntentBuilder("VirginRadioIntent").\
                     require("ItaradioKeyword").require("PlayKeyword").build()
        self.register_intent(VirginRadio_intent, self.handle_VirginRadio_intent)

 def handle_whatson_Discoradio_intent(self, message):
        r = requests.get('http://46.37.20.206:1935/live/1discoradio.stream/playlist.m3u8')
        j = r.json()
def handle_whatson_LifeGateRadio_intent(self, message):
        r = requests.get('http://onair11.xdevel.com:8024')
        j = r.json()
def handle_whatson_R101Diretta_intent(self, message):
        r = requests.get('http://icecast.unitedradio.it/r101')
        j = r.json()
def handle_whatson_Radio105_intent(self, message):
        r = requests.get('http://icecast.105.net/105.mp3')
        j = r.json()
def handle_whatson_Radio24_intent(self, message):
        r = requests.get('http://shoutcast.radio24.it:8000/listen.pls')
        j = r.json()
def handle_whatson_RadioAmoreCampania_intent(self, message):
        r = requests.get('http://onair11.xdevel.com:8002')
        j = r.json()
def handle_whatson_RadioCapital_intent(self, message):
        r = requests.get('http://radiocapital-lh.akamaihd.net/i/RadioCapital_Live_1@196312/master.m3u8')
        j = r.json()
def handle_whatson_RadioCuore_intent(self, message):
        r = requests.get('http://nr9.newradio.it:9029')
        j = r.json()
def handle_whatson_RadioDeejay_intent(self, message):
        r = requests.get('http://radiodeejay-lh.akamaihd.net/i/RadioDeejay_Live_1@189857/master.m3u8')
        j = r.json()
def handle_whatson_RadioIbiza_intent(self, message):
        r = requests.get('http://wma02.fluidstream.net:5010/')
        j = r.json()
def handle_whatson_RadioKissKissItalia_intent(self, message):
        r = requests.get('http://wma07.fluidstream.net:3616/;stream.nsv')
        j = r.json()
def handle_whatson_RadioKissKissNapoli_intent(self, message):
        r = requests.get('http://ice08.fluidstream.net/KKNapoli.aac')
        j = r.json()
def handle_whatson_RadioKissKiss_intent(self, message):
        r = requests.get('http://ice07.fluidstream.net:8080/KissKiss.mp3')
        j = r.json()
def handle_whatson_RadioLatteMiele_intent(self, message):
        r = requests.get('http://onair18.xdevel.com:8014/')
        j = r.json()
def handle_whatson_Radiom2o_intent(self, message):
        r = requests.get('http://radiom2o-lh.akamaihd.net/i/RadioM2o_Live_1@42518/master.m3u8')
        j = r.json()
def handle_whatson_RadioMarte_intent(self, message):
        r = requests.get('http://onair18.xdevel.com:8212/')
        j = r.json()
def handle_whatson_RadioPlaystudio_intent(self, message):
        r = requests.get('http://playstudio.serverroom.us:4140')
        j = r.json()
def handle_whatson_RadioRCSl’OndaVeronese_intent(self, message):
        r = requests.get('http://176.31.254.217:8030/')
        j = r.json()
def handle_whatson_RadioSportiva_intent(self, message):
        r = requests.get('http://nr5.newradio.it:8545/stream.mp3')
        j = r.json()
def handle_whatson_RadioStudioDelta_intent(self, message):
        r = requests.get('http://5.63.145.172:7203/')
        j = r.json()
def handle_whatson_RadioSubasio_intent(self, message):
        r = requests.get('http://onair18.xdevel.com:8152')
        j = r.json()
def handle_whatson_RadioZetalItaliana_intent(self, message):
        r = requests.get('http://shoutcast.rtl.it:3030/stream/1/')
        j = r.json()
def handle_whatson_RadionorbaMusicSport_intent(self, message):
        r = requests.get('http://onair7.xdevel.com:8738/')
        j = r.json()
def handle_whatson_Radionorba_intent(self, message):
        r = requests.get('http://onair11.xdevel.com:9990/')
        j = r.json()
def handle_whatson_RaiGrParlamento_intent(self, message):
        r = requests.get('http://icestreaming.rai.it/7.mp3')
        j = r.json()
def handle_whatson_RaiIsoRadio_intent(self, message):
        r = requests.get('http://icestreaming.rai.it/6.mp3')
        j = r.json()
def handle_whatson_RaiRadio1_intent(self, message):
        r = requests.get('http://icestreaming.rai.it/1.mp3')
        j = r.json()
def handle_whatson_RaiRadio2_intent(self, message):
        r = requests.get('http://icestreaming.rai.it/2.mp3')
        j = r.json()
def handle_whatson_RaiRadio3_intent(self, message):
        r = requests.get('http://icestreaming.rai.it/3.mp3')
        j = r.json()
def handle_whatson_RaiRadio4Light_intent(self, message):
        r = requests.get('http://icestreaming.rai.it/4.mp3')
        j = r.json()
def handle_whatson_RaiRadio5Classica_intent(self, message):
        r = requests.get('http://icestreaming.rai.it/5.mp3')
        j = r.json()
def handle_whatson_RaiRadio6Teca_intent(self, message):
        r = requests.get('http://icestreaming.rai.it:80/9.mp3')
        j = r.json()
def handle_whatson_RaiRadio7Live_intent(self, message):
        r = requests.get('http://icestreaming.rai.it:80/10.mp3')
        j = r.json()
def handle_whatson_RaiRadio8Opera_intent(self, message):
        r = requests.get('http://icestreaming.rai.it:80/11.mp3')
        j = r.json()
def handle_whatson_RamPower1027_intent(self, message):
        r = requests.get('http://46.37.20.206:1935/live/1ram.stream/playlist.m3u8')
        j = r.json()
def handle_whatson_RDS_intent(self, message):
        r = requests.get('http://www.rds.it:8000/stream')
        j = r.json()
def handle_whatson_RINRadioItaliaNetwork_intent(self, message):
        r = requests.get('http://sr9.inmystream.info:8006')
        j = r.json()
def handle_whatson_RMCRadioMonteCarlo_intent(self, message):
        r = requests.get('http://edge.radiomontecarlo.net/RMC.mp3')
        j = r.json()
def handle_whatson_RMC2RadioMonteCarlo2_intent(self, message):
        r = requests.get('http://edge.radiomontecarlo.net/MC2.mp3')
        j = r.json()
def handle_whatson_RTLBest_intent(self, message):
        r = requests.get('http://shoutcast.rtl.it:3020/')
        j = r.json()
def handle_whatson_RTLGroove_intent(self, message):
        r = requests.get('http://shoutcast.rtl.it:3040/')
        j = r.json()
def handle_whatson_RTLItalianStyle_intent(self, message):
        r = requests.get('http://shoutcast.rtl.it:3030/')
        j = r.json()
def handle_whatson_RTLLounge_intent(self, message):
        r = requests.get('http://shoutcast.rtl.it:3070/')
        j = r.json()
def handle_whatson_RTLRadiofreccia_intent(self, message):
        r = requests.get('http://shoutcast.rtl.it:3060/')
        j = r.json()
def handle_whatson_RTL_intent(self, message):
        r = requests.get('http://shoutcast.rtl.it:3010/')
        j = r.json()
def handle_whatson_StudioradioTheVintageStation_intent(self, message):
        r = requests.get('http://91.121.38.216:8060/')
        j = r.json()
def handle_whatson_VirginRadio_intent(self, message):
        r = requests.get('http://icecast.unitedradio.it/Virgin.mp3')
        j = r.json()

    def handle_Discoradio_intent(self, message):
        if self.audioservice:
            self.audioservice.play(Discoradio_URL, message.data['utterance'])
        else:
            self.process = play_mp3(Discoradio_URL)
def handle_LifeGateRadio_intent(self, message):
        if self.audioservice:
            self.audioservice.play(LifeGateRadio_URL, message.data['utterance'])
        else:
            self.process = play_mp3(LifeGateRadio_URL)
def handle_R101Diretta_intent(self, message):
        if self.audioservice:
            self.audioservice.play(R101Diretta_URL, message.data['utterance'])
        else:
            self.process = play_mp3(R101Diretta_URL)
def handle_Radio105_intent(self, message):
        if self.audioservice:
            self.audioservice.play(Radio105_URL, message.data['utterance'])
        else:
            self.process = play_mp3(Radio105_URL)
def handle_Radio24_intent(self, message):
        if self.audioservice:
            self.audioservice.play(Radio24_URL, message.data['utterance'])
        else:
            self.process = play_mp3(Radio24_URL)
def handle_RadioAmoreCampania_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RadioAmoreCampania_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RadioAmoreCampania_URL)
def handle_RadioCapital_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RadioCapital_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RadioCapital_URL)
def handle_RadioCuore_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RadioCuore_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RadioCuore_URL)
def handle_RadioDeejay_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RadioDeejay_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RadioDeejay_URL)
def handle_RadioIbiza_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RadioIbiza_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RadioIbiza_URL)
def handle_RadioKissKissItalia_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RadioKissKissItalia_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RadioKissKissItalia_URL)
def handle_RadioKissKissNapoli_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RadioKissKissNapoli_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RadioKissKissNapoli_URL)
def handle_RadioKissKiss_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RadioKissKiss_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RadioKissKiss_URL)
def handle_RadioLatteMiele_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RadioLatteMiele_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RadioLatteMiele_URL)
def handle_Radiom2o_intent(self, message):
        if self.audioservice:
            self.audioservice.play(Radiom2o_URL, message.data['utterance'])
        else:
            self.process = play_mp3(Radiom2o_URL)
def handle_RadioMarte_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RadioMarte_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RadioMarte_URL)
def handle_RadioPlaystudio_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RadioPlaystudio_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RadioPlaystudio_URL)
def handle_RadioRCSlOndaVeronese_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RadioRCSl’OndaVeronese_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RadioRCSl’OndaVeronese_URL)
def handle_RadioSportiva_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RadioSportiva_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RadioSportiva_URL)
def handle_RadioStudioDelta_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RadioStudioDelta_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RadioStudioDelta_URL)
def handle_RadioSubasio_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RadioSubasio_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RadioSubasio_URL)
def handle_RadioZetalItaliana_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RadioZetalItaliana_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RadioZetalItaliana_URL)
def handle_RadionorbaMusicSport_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RadionorbaMusic&Sport_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RadionorbaMusic&Sport_URL)
def handle_Radionorba_intent(self, message):
        if self.audioservice:
            self.audioservice.play(Radionorba_URL, message.data['utterance'])
        else:
            self.process = play_mp3(Radionorba_URL)
def handle_RaiGrParlamento_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RaiGrParlamento_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RaiGrParlamento_URL)
def handle_RaiIsoRadio_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RaiIsoRadio_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RaiIsoRadio_URL)
def handle_RaiRadio1_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RaiRadio1_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RaiRadio1_URL)
def handle_RaiRadio2_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RaiRadio2_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RaiRadio2_URL)
def handle_RaiRadio3_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RaiRadio3_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RaiRadio3_URL)
def handle_RaiRadio4Light_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RaiRadio4Light_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RaiRadio4Light_URL)
def handle_RaiRadio5Classica_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RaiRadio5Classica_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RaiRadio5Classica_URL)
def handle_RaiRadio6Teca_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RaiRadio6Teca_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RaiRadio6Teca_URL)
def handle_RaiRadio7Live_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RaiRadio7Live_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RaiRadio7Live_URL)
def handle_RaiRadio8Opera_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RaiRadio8Opera_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RaiRadio8Opera_URL)
def handle_RamPower1027_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RamPower1027_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RamPower1027_URL)
def handle_RDS_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RDS_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RDS_URL)
def handle_RINRadioItaliaNetwork_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RINRadioItaliaNetwork_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RINRadioItaliaNetwork_URL)
def handle_RMCRadioMonteCarlo_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RMCRadioMonteCarlo_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RMCRadioMonteCarlo_URL)
def handle_RMC2RadioMonteCarlo2_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RMC2RadioMonteCarlo2_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RMC2RadioMonteCarlo2_URL)
def handle_RTLBest_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RTLBest_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RTLBest_URL)
def handle_RTLGroove_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RTLGroove_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RTLGroove_URL)
def handle_RTLItalianStyle_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RTLItalianStyle_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RTLItalianStyle_URL)
def handle_RTLLounge_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RTLLounge_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RTLLounge_URL)
def handle_RTLRadiofreccia_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RTLRadiofreccia_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RTLRadiofreccia_URL)
def handle_RTL_intent(self, message):
        if self.audioservice:
            self.audioservice.play(RTL_URL, message.data['utterance'])
        else:
            self.process = play_mp3(RTL_URL)
def handle_StudioradioTheVintageStation_intent(self, message):
        if self.audioservice:
            self.audioservice.play(StudioradioTheVintageStation_URL, message.data['utterance'])
        else:
            self.process = play_mp3(StudioradioTheVintageStation_URL)
def handle_VirginRadio_intent(self, message):
        if self.audioservice:
            self.audioservice.play(VirginRadio_URL, message.data['utterance'])
        else:
            self.process = play_mp3(VirginRadio_URL)

    def stop(self):
        pass


def create_skill():
    return ItaradioSkill()
