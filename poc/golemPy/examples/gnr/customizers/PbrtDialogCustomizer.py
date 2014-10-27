import logging

from examples.gnr.ui.PbrtDialog import PbrtDialog
from examples.gnr.task.PbrtGNRTask import PbrtRenderOptions

logger = logging.getLogger(__name__)

class PbrtDialogCustomizer:
    #############################
    def __init__( self, gui, logic, newTaskDialog ):

        assert isinstance( gui, PbrtDialog )

        self.gui = gui
        self.logic = logic
        self.newTaskDialog = newTaskDialog

        self.__init()
        self.__setupConnections()

    #############################
    def __init( self ):
        renderer = self.logic.getRenderer( u"PBRT" )
        self.rendererOptions = renderer.options
        self.gui.ui.pixelFilterComboBox.clear()
        self.gui.ui.pixelFilterComboBox.addItems( renderer.filters )
        pixelFilterItem = self.gui.ui.pixelFilterComboBox.findText( self.rendererOptions.pixelFilter )
        if pixelFilterItem >= 0:
            self.gui.ui.pixelFilterComboBox.setCurrentIndex( pixelFilterItem )

        self.gui.ui.pathTracerComboBox.clear()
        self.gui.ui.pathTracerComboBox.addItems( renderer.pathTracers )

        algItem = self.gui.ui.pathTracerComboBox.findText( self.rendererOptions.algorithmType )

        if algItem >= 0:
            self.gui.ui.pathTracerComboBox.setCurrentIndex( algItem )

        self.gui.ui.samplesPerPixelSpinBox.setValue( self.rendererOptions.samplesPerPixelCount )

    #############################
    def __setupConnections( self ):
        self.gui.ui.buttonBox.rejected.connect( self.gui.window.close )
        self.gui.ui.buttonBox.accepted.connect( lambda: self.__changeRendererOptions() )

    #############################
    def __changeRendererOptions( self ):
        self.rendererOptions.pixelFilter = u"{}".format( self.gui.ui.pixelFilterComboBox.itemText( self.gui.ui.pixelFilterComboBox.currentIndex() ) )
        self.rendererOptions.samplesPerPixelCount = self.gui.ui.samplesPerPixelSpinBox.value()
        self.rendererOptions.algorithmType = u"{}".format( self.gui.ui.pathTracerComboBox.itemText( self.gui.ui.pathTracerComboBox.currentIndex() ) )
        self.newTaskDialog.setRendererOptions( self.rendererOptions )
        self.gui.window.close()