# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class loginFrame
###########################################################################

class loginFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 588,408 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"- Selamat Datang di Aplikasi Pemesanan Paket Wisata Indonesia - #1 Aplikasi Wisata yang Mudah dan Praktis -", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_staticText2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"LOGIN" ), wx.VERTICAL )

		self.m_staticText31 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		sbSizer3.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.text_email = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,50 ), 0|wx.BORDER_NONE )
		self.text_email.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		sbSizer3.Add( self.text_email, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		sbSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.text_password = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,50 ), wx.TE_PASSWORD|wx.BORDER_NONE )
		self.text_password.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		sbSizer3.Add( self.text_password, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_login = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.btn_login.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.btn_login.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		sbSizer3.Add( self.btn_login, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_go_to_register = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Apakah kamu masih belum memiliki akun? Daftar disini.", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.btn_go_to_register, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( sbSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_login.Bind( wx.EVT_BUTTON, self.btn_login_onclick )
		self.btn_go_to_register.Bind( wx.EVT_BUTTON, self.btn_go_to_register_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_login_onclick( self, event ):
		event.Skip()

	def btn_go_to_register_onclick( self, event ):
		event.Skip()


###########################################################################
## Class daftarForm
###########################################################################

class daftarForm ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 588,564 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"DAFTAR" ), wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Nama Lengkap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		sbSizer3.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.text_fullname = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), 0|wx.BORDER_NONE )
		self.text_fullname.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		sbSizer3.Add( self.text_fullname, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Nomor KTP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		sbSizer3.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.text_noktp = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), 0|wx.BORDER_NONE )
		self.text_noktp.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		sbSizer3.Add( self.text_noktp, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Nomor HP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		sbSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.text_nohp = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), 0|wx.BORDER_NONE )
		self.text_nohp.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		sbSizer3.Add( self.text_nohp, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText8 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"E-mail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		sbSizer3.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.text_email = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), 0|wx.BORDER_NONE )
		self.text_email.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		sbSizer3.Add( self.text_email, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		sbSizer3.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.text_password = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), 0|wx.BORDER_NONE )
		self.text_password.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		sbSizer3.Add( self.text_password, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText10 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Konfirmasi password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		sbSizer3.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.text_confirm_password = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), wx.TE_PASSWORD|wx.BORDER_NONE )
		self.text_confirm_password.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		sbSizer3.Add( self.text_confirm_password, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_register = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"DAFTAR", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.btn_register.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.btn_register.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		sbSizer3.Add( self.btn_register, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_go_to_login = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Apakah kamu sudah memiliki akun? Login disini.", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.btn_go_to_login, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( sbSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_register.Bind( wx.EVT_BUTTON, self.btn_register_onclick )
		self.btn_go_to_login.Bind( wx.EVT_BUTTON, self.btn_go_to_login_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_register_onclick( self, event ):
		event.Skip()

	def btn_go_to_login_onclick( self, event ):
		event.Skip()


###########################################################################
## Class beranda
###########################################################################

class beranda ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,346 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"BERANDA" ), wx.VERTICAL )

		self.btn_order_now = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Pesan Paket Wisata Sekarang! ", wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		self.btn_order_now.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.btn_order_now.SetBackgroundColour( wx.Colour( 7, 139, 248 ) )

		sbSizer4.Add( self.btn_order_now, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_order_history = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Riwayat Pesanan ", wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		self.btn_order_history.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.btn_order_history.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		sbSizer4.Add( self.btn_order_history, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_confirm_payment = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Konfirmasi Pembayaran Pesanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btn_confirm_payment, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_cancel_order = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Ajukan Pembatalan Pesanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btn_cancel_order, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer4.Add( gSizer2, 1, wx.EXPAND, 5 )

		self.btn_logout = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Keluar Akun", wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		self.btn_logout.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.btn_logout.SetBackgroundColour( wx.Colour( 236, 0, 6 ) )

		sbSizer4.Add( self.btn_logout, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( sbSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_order_now.Bind( wx.EVT_BUTTON, self.btn_order_now_onclick )
		self.btn_order_history.Bind( wx.EVT_BUTTON, self.btn_order_history_onclick )
		self.btn_confirm_payment.Bind( wx.EVT_BUTTON, self.btn_confirm_payment_onclick )
		self.btn_cancel_order.Bind( wx.EVT_BUTTON, self.btn_cancel_order_onclick )
		self.btn_logout.Bind( wx.EVT_BUTTON, self.btn_logout_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_order_now_onclick( self, event ):
		event.Skip()

	def btn_order_history_onclick( self, event ):
		event.Skip()

	def btn_confirm_payment_onclick( self, event ):
		event.Skip()

	def btn_cancel_order_onclick( self, event ):
		event.Skip()

	def btn_logout_onclick( self, event ):
		event.Skip()


###########################################################################
## Class Pesan
###########################################################################

class Pesan  ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,341 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Pilih Paket Wisatamu" ), wx.VERTICAL )

		self.m_radioBtn4 = wx.RadioButton( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Jember 3 Hari (3 Hari)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_radioBtn4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		sbSizer5.Add( self.m_radioBtn4, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_radioBtn42 = wx.RadioButton( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Jember 1 Minggu (7 Hari)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_radioBtn42, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_radioBtn43 = wx.RadioButton( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Malang 3 Hari (3 Hari)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_radioBtn43, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_radioBtn44 = wx.RadioButton( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Malang 1 Minggu (7 Hari)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_radioBtn44, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_radioBtn45 = wx.RadioButton( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Yogyakarta 3 Hari (3 Hari)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_radioBtn45, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_radioBtn41 = wx.RadioButton( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Yogyakarta 1 Minggu (7 Hari)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_radioBtn41, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button19 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button19, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button20 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Selanjutnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_button20.SetBackgroundColour( wx.Colour( 0, 128, 255 ) )

		gSizer3.Add( self.m_button20, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer5.Add( gSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class Pesan2
###########################################################################

class Pesan2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,399 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tanggal Pesan (Format = YYYY-MM-DD)" ), wx.VERTICAL )

		self.m_textCtrl31 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_textCtrl31, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( sbSizer8, 1, wx.EXPAND, 5 )

		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Berapa Orang?" ), wx.VERTICAL )

		m_comboBox1Choices = [ u"1", u"2", u"3", u"4" ]
		self.m_comboBox1 = wx.ComboBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetSelection( 3 )
		sbSizer9.Add( self.m_comboBox1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( sbSizer9, 1, wx.EXPAND, 5 )

		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Orang 1" ), wx.VERTICAL )

		self.m_textCtrl35 = wx.TextCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Nama Lengkap", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.m_textCtrl35, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl36 = wx.TextCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Nomor KTP", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.m_textCtrl36, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer4.Add( sbSizer12, 1, wx.EXPAND, 5 )

		sbSizer121 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Orang 1" ), wx.VERTICAL )

		self.m_textCtrl351 = wx.TextCtrl( sbSizer121.GetStaticBox(), wx.ID_ANY, u"Nama Lengkap", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer121.Add( self.m_textCtrl351, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl361 = wx.TextCtrl( sbSizer121.GetStaticBox(), wx.ID_ANY, u"Nomor KTP", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer121.Add( self.m_textCtrl361, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer4.Add( sbSizer121, 1, wx.EXPAND, 5 )

		sbSizer122 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Orang 1" ), wx.VERTICAL )

		self.m_textCtrl352 = wx.TextCtrl( sbSizer122.GetStaticBox(), wx.ID_ANY, u"Nama Lengkap", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer122.Add( self.m_textCtrl352, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl362 = wx.TextCtrl( sbSizer122.GetStaticBox(), wx.ID_ANY, u"Nomor KTP", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer122.Add( self.m_textCtrl362, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer4.Add( sbSizer122, 1, wx.EXPAND, 5 )

		sbSizer123 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Orang 1" ), wx.VERTICAL )

		self.m_textCtrl353 = wx.TextCtrl( sbSizer123.GetStaticBox(), wx.ID_ANY, u"Nama Lengkap", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer123.Add( self.m_textCtrl353, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl363 = wx.TextCtrl( sbSizer123.GetStaticBox(), wx.ID_ANY, u"Nomor KTP", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer123.Add( self.m_textCtrl363, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer4.Add( sbSizer123, 1, wx.EXPAND, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button23.SetMaxSize( wx.Size( -1,30 ) )

		gSizer4.Add( self.m_button23, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"Pesan !", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button24.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_button24.SetBackgroundColour( wx.Colour( 0, 128, 255 ) )
		self.m_button24.SetMaxSize( wx.Size( -1,30 ) )

		gSizer4.Add( self.m_button24, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( gSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class kodeBooking
###########################################################################

class kodeBooking ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,260 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		sbSizer37 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Keterangan Pesanan" ), wx.VERTICAL )

		self.m_textCtrl57 = wx.TextCtrl( sbSizer37.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer37.Add( self.m_textCtrl57, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer5.Add( sbSizer37, 1, wx.EXPAND, 5 )

		sbSizer38 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Kode Booking" ), wx.VERTICAL )

		self.m_textCtrl58 = wx.TextCtrl( sbSizer38.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer38.Add( self.m_textCtrl58, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer5.Add( sbSizer38, 1, wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button25 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button25, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button26 = wx.Button( self, wx.ID_ANY, u"Selesai (Kembali ke Beranda)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button26.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_button26.SetBackgroundColour( wx.Colour( 0, 128, 255 ) )

		gSizer5.Add( self.m_button26, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer5.Add( gSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class riwayatPesanan
###########################################################################

class riwayatPesanan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		sbSizer40 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Riwayat Pesanan" ), wx.VERTICAL )

		self.m_textCtrl65 = wx.TextCtrl( sbSizer40.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer40.Add( self.m_textCtrl65, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( sbSizer40, 1, wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button29 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button29, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button30 = wx.Button( self, wx.ID_ANY, u"Lihat Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button30.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_button30.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		gSizer9.Add( self.m_button30, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( gSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class detailPesanan
###########################################################################

class detailPesanan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		sbSizer41 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Masukkan Kode Booking" ), wx.VERTICAL )

		self.m_textCtrl66 = wx.TextCtrl( sbSizer41.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		sbSizer41.Add( self.m_textCtrl66, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button36 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Cek Kode Booking", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer41.Add( self.m_button36, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( sbSizer41, 1, wx.EXPAND, 5 )

		sbSizer42 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Detail Pesanan" ), wx.VERTICAL )

		self.m_textCtrl67 = wx.TextCtrl( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer42.Add( self.m_textCtrl67, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( sbSizer42, 1, wx.EXPAND, 5 )

		self.m_button33 = wx.Button( self, wx.ID_ANY, u"Selesai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_button33.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer7.Add( self.m_button33, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class buktiPembayaran
###########################################################################

class buktiPembayaran ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		sbSizer41 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Masukkan Kode Booking" ), wx.VERTICAL )

		self.m_textCtrl66 = wx.TextCtrl( sbSizer41.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		sbSizer41.Add( self.m_textCtrl66, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button36 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Cek Kode Booking", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer41.Add( self.m_button36, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( sbSizer41, 1, wx.EXPAND, 5 )

		sbSizer42 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Detail Pesanan" ), wx.VERTICAL )

		self.m_textCtrl67 = wx.TextCtrl( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer42.Add( self.m_textCtrl67, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( sbSizer42, 1, wx.EXPAND, 5 )

		gSizer11 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button49 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_button49, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button33 = wx.Button( self, wx.ID_ANY, u"Selanjutnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_button33.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		gSizer11.Add( self.m_button33, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( gSizer11, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class buktiPembayaran2
###########################################################################

class buktiPembayaran2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,152 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		sbSizer41 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Masukkan Nomor Bukti Pembayaran" ), wx.VERTICAL )

		self.m_textCtrl66 = wx.TextCtrl( sbSizer41.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		sbSizer41.Add( self.m_textCtrl66, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( sbSizer41, 0, wx.EXPAND, 5 )

		self.m_button33 = wx.Button( self, wx.ID_ANY, u"Selesai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_button33.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer7.Add( self.m_button33, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class ajukanPembatalan
###########################################################################

class ajukanPembatalan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		sbSizer41 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Masukkan Kode Booking" ), wx.VERTICAL )

		self.m_textCtrl66 = wx.TextCtrl( sbSizer41.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		sbSizer41.Add( self.m_textCtrl66, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button36 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Cek Kode Booking", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer41.Add( self.m_button36, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( sbSizer41, 1, wx.EXPAND, 5 )

		sbSizer42 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Detail Pesanan" ), wx.VERTICAL )

		self.m_textCtrl67 = wx.TextCtrl( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer42.Add( self.m_textCtrl67, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( sbSizer42, 1, wx.EXPAND, 5 )

		gSizer11 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button49 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_button49, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button33 = wx.Button( self, wx.ID_ANY, u"Ajukan Pembatalan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_button33.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		gSizer11.Add( self.m_button33, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( gSizer11, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


