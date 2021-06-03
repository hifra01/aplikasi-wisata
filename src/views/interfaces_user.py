# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class loginFrame
###########################################################################

class loginFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login - Aplikasi Wisata", pos = wx.DefaultPosition, size = wx.Size( 588,408 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Register - Aplikasi Wisata", pos = wx.DefaultPosition, size = wx.Size( 588,564 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

		self.text_password = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), wx.TE_PASSWORD|wx.BORDER_NONE )
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Beranda (Customer) - Aplikasi Wisata", pos = wx.DefaultPosition, size = wx.Size( 500,346 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

class Pesan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pesan Tiket - Aplikasi Wisata", pos = wx.DefaultPosition, size = wx.Size( 500,552 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Pilih Paket Wisatamu" ), wx.VERTICAL )

		combobox_paket_wisataChoices = [ wx.EmptyString ]
		self.combobox_paket_wisata = wx.ComboBox( sbSizer5.GetStaticBox(), wx.ID_ANY, u"-- Pilih Paket Wisata --", wx.DefaultPosition, wx.DefaultSize, combobox_paket_wisataChoices, wx.CB_DROPDOWN )
		self.combobox_paket_wisata.SetSelection( 0 )
		sbSizer5.Add( self.combobox_paket_wisata, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer10.Add( sbSizer5, 1, wx.EXPAND, 5 )

		sbSizer51 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tanggal Berangkat" ), wx.VERTICAL )

		self.calendar_tanggal_berangkat = wx.adv.CalendarCtrl( sbSizer51.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer51.Add( self.calendar_tanggal_berangkat, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer10.Add( sbSizer51, 1, wx.EXPAND, 5 )

		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Peserta" ), wx.VERTICAL )

		self.list_daftar_peserta = wx.ListCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		sbSizer8.Add( self.list_daftar_peserta, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer16 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_add_person = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Tambah Peserta", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer16.Add( self.btn_add_person, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_delete_person = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Hapus Peserta", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer16.Add( self.btn_delete_person, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer8.Add( gSizer16, 1, wx.EXPAND, 5 )


		bSizer10.Add( sbSizer8, 1, wx.EXPAND, 5 )

		gSizer31 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_back = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.btn_back, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_make_order = wx.Button( self, wx.ID_ANY, u"Pesan Paket Sekarang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_make_order.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.btn_make_order.SetBackgroundColour( wx.Colour( 0, 128, 255 ) )

		gSizer31.Add( self.btn_make_order, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer10.Add( gSizer31, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.list_daftar_peserta.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.list_daftar_peserta_on_item_deselected )
		self.list_daftar_peserta.Bind( wx.EVT_LIST_ITEM_SELECTED, self.list_daftar_peserta_on_item_selected )
		self.btn_add_person.Bind( wx.EVT_BUTTON, self.btn_add_person_onclick )
		self.btn_delete_person.Bind( wx.EVT_BUTTON, self.btn_delete_person_onclick )
		self.btn_back.Bind( wx.EVT_BUTTON, self.btn_back_onclick )
		self.btn_make_order.Bind( wx.EVT_BUTTON, self.btn_make_order_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def list_daftar_peserta_on_item_deselected( self, event ):
		event.Skip()

	def list_daftar_peserta_on_item_selected( self, event ):
		event.Skip()

	def btn_add_person_onclick( self, event ):
		event.Skip()

	def btn_delete_person_onclick( self, event ):
		event.Skip()

	def btn_back_onclick( self, event ):
		event.Skip()

	def btn_make_order_onclick( self, event ):
		event.Skip()


###########################################################################
## Class PesanTambahOrang
###########################################################################

class PesanTambahOrang ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tambah Peserta", pos = wx.DefaultPosition, size = wx.Size( 342,227 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tambah Orang" ), wx.VERTICAL )

		sbSizer44 = wx.StaticBoxSizer( wx.StaticBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Nama" ), wx.VERTICAL )

		self.text_name = wx.TextCtrl( sbSizer44.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer44.Add( self.text_name, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer8.Add( sbSizer44, 1, wx.EXPAND, 5 )

		sbSizer45 = wx.StaticBoxSizer( wx.StaticBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"No KTP" ), wx.VERTICAL )

		self.text_no_ktp = wx.TextCtrl( sbSizer45.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_no_ktp.SetMaxLength( 16 )
		sbSizer45.Add( self.text_no_ktp, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer8.Add( sbSizer45, 1, wx.EXPAND, 5 )

		self.btn_add_new_person = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Tambah Orang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_add_new_person.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.btn_add_new_person.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		sbSizer8.Add( self.btn_add_new_person, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( sbSizer8, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_add_new_person.Bind( wx.EVT_BUTTON, self.btn_add_new_person_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_add_new_person_onclick( self, event ):
		event.Skip()


###########################################################################
## Class Pesan3
###########################################################################

class Pesan3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,399 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tambah Orang" ), wx.VERTICAL )

		sbSizer44 = wx.StaticBoxSizer( wx.StaticBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Nama" ), wx.VERTICAL )

		self.m_textCtrl51 = wx.TextCtrl( sbSizer44.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer44.Add( self.m_textCtrl51, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer8.Add( sbSizer44, 1, wx.EXPAND, 5 )

		sbSizer45 = wx.StaticBoxSizer( wx.StaticBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"No KTP" ), wx.VERTICAL )

		self.m_textCtrl52 = wx.TextCtrl( sbSizer45.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer45.Add( self.m_textCtrl52, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer8.Add( sbSizer45, 1, wx.EXPAND, 5 )

		self.m_button36 = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Tambah Orang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button36.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_button36.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		sbSizer8.Add( self.m_button36, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( sbSizer8, 1, wx.EXPAND, 5 )


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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Riwayat Pesanan - Aplikasi Wisata", pos = wx.DefaultPosition, size = wx.Size( 474,299 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		sbSizer40 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Riwayat Pesanan" ), wx.VERTICAL )

		self.list_order_history = wx.ListCtrl( sbSizer40.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		sbSizer40.Add( self.list_order_history, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( sbSizer40, 1, wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_back = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.btn_back, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_order_detail = wx.Button( self, wx.ID_ANY, u"Lihat Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_order_detail.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.btn_order_detail.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		gSizer9.Add( self.btn_order_detail, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( gSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.list_order_history.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.list_order_history_on_item_deselected )
		self.list_order_history.Bind( wx.EVT_LIST_ITEM_SELECTED, self.list_order_history_on_item_selected )
		self.btn_back.Bind( wx.EVT_BUTTON, self.btn_back_onclick )
		self.btn_order_detail.Bind( wx.EVT_BUTTON, self.btn_order_detail_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def list_order_history_on_item_deselected( self, event ):
		event.Skip()

	def list_order_history_on_item_selected( self, event ):
		event.Skip()

	def btn_back_onclick( self, event ):
		event.Skip()

	def btn_order_detail_onclick( self, event ):
		event.Skip()


###########################################################################
## Class detailPesanan
###########################################################################

class detailPesanan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Detail Pesanan - Aplikasi Wisata", pos = wx.DefaultPosition, size = wx.Size( 500,654 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		sbSizer20 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Kode Booking" ), wx.VERTICAL )

		self.text_kode_booking = wx.TextCtrl( sbSizer20.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer20.Add( self.text_kode_booking, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer20, 1, wx.EXPAND, 5 )

		sbSizer201 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Paket Wisata" ), wx.VERTICAL )

		self.text_paket_wisata = wx.TextCtrl( sbSizer201.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer201.Add( self.text_paket_wisata, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer201, 1, wx.EXPAND, 5 )

		sbSizer202 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tanggal Berangkat" ), wx.VERTICAL )

		self.text_tanggal_berangkat = wx.TextCtrl( sbSizer202.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer202.Add( self.text_tanggal_berangkat, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer202, 1, wx.EXPAND, 5 )

		sbSizer203 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tanggal Pulang" ), wx.VERTICAL )

		self.text_tanggal_pulang = wx.TextCtrl( sbSizer203.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer203.Add( self.text_tanggal_pulang, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer203, 1, wx.EXPAND, 5 )

		sbSizer204 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Status" ), wx.VERTICAL )

		self.text_status = wx.TextCtrl( sbSizer204.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer204.Add( self.text_status, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer204, 1, wx.EXPAND, 5 )

		sbSizer205 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Destinasi Wisata" ), wx.VERTICAL )

		self.list_destinasi_wisata = wx.ListCtrl( sbSizer205.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		sbSizer205.Add( self.list_destinasi_wisata, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer205, 1, wx.EXPAND, 5 )

		sbSizer2051 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Peserta" ), wx.VERTICAL )

		self.list_peserta = wx.ListCtrl( sbSizer2051.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		sbSizer2051.Add( self.list_peserta, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer2051, 1, wx.EXPAND, 5 )

		self.btn_back = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.btn_back, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer29 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_back.Bind( wx.EVT_BUTTON, self.btn_back_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_back_onclick( self, event ):
		event.Skip()


###########################################################################
## Class ajukanPembatalan
###########################################################################

class ajukanPembatalan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		sbSizer40 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Riwayat Pesanan" ), wx.VERTICAL )

		self.list_order_history = wx.ListCtrl( sbSizer40.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		sbSizer40.Add( self.list_order_history, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( sbSizer40, 1, wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_back = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.btn_back, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_order_detail = wx.Button( self, wx.ID_ANY, u"Lihat Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_order_detail.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.btn_order_detail.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		gSizer9.Add( self.btn_order_detail, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( gSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.list_order_history.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.list_order_history_on_item_deselected )
		self.list_order_history.Bind( wx.EVT_LIST_ITEM_SELECTED, self.list_order_history_on_item_selected )
		self.btn_back.Bind( wx.EVT_BUTTON, self.btn_back_onclick )
		self.btn_order_detail.Bind( wx.EVT_BUTTON, self.btn_order_detail_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def list_order_history_on_item_deselected( self, event ):
		event.Skip()

	def list_order_history_on_item_selected( self, event ):
		event.Skip()

	def btn_back_onclick( self, event ):
		event.Skip()

	def btn_order_detail_onclick( self, event ):
		event.Skip()


###########################################################################
## Class pembatalanDetail
###########################################################################

class pembatalanDetail ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		sbSizer20 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Kode Booking" ), wx.VERTICAL )

		self.text_kode_booking = wx.TextCtrl( sbSizer20.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer20.Add( self.text_kode_booking, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer20, 1, wx.EXPAND, 5 )

		sbSizer201 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Paket Wisata" ), wx.VERTICAL )

		self.text_paket_wisata = wx.TextCtrl( sbSizer201.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer201.Add( self.text_paket_wisata, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer201, 1, wx.EXPAND, 5 )

		sbSizer202 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tanggal Berangkat" ), wx.VERTICAL )

		self.text_tanggal_berangkat = wx.TextCtrl( sbSizer202.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer202.Add( self.text_tanggal_berangkat, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer202, 1, wx.EXPAND, 5 )

		sbSizer203 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tanggal Pulang" ), wx.VERTICAL )

		self.text_tanggal_pulang = wx.TextCtrl( sbSizer203.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer203.Add( self.text_tanggal_pulang, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer203, 1, wx.EXPAND, 5 )

		sbSizer204 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Status" ), wx.VERTICAL )

		self.text_status = wx.TextCtrl( sbSizer204.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer204.Add( self.text_status, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer204, 1, wx.EXPAND, 5 )

		sbSizer205 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Destinasi Wisata" ), wx.VERTICAL )

		self.list_destinasi_wisata = wx.ListCtrl( sbSizer205.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,100 ), wx.LC_REPORT )
		sbSizer205.Add( self.list_destinasi_wisata, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer205, 1, wx.EXPAND, 5 )

		sbSizer2051 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Peserta" ), wx.VERTICAL )

		self.list_peserta = wx.ListCtrl( sbSizer2051.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,100 ), wx.LC_REPORT )
		sbSizer2051.Add( self.list_peserta, 0, wx.EXPAND|wx.ALL, 5 )


		bSizer29.Add( sbSizer2051, 1, wx.EXPAND, 5 )

		self.btn_cancel_order = wx.Button( self, wx.ID_ANY, u"Batalkan Pesanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_cancel_order.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.btn_cancel_order.SetBackgroundColour( wx.Colour( 232, 0, 5 ) )

		bSizer29.Add( self.btn_cancel_order, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_back = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.btn_back, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer29 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_cancel_order.Bind( wx.EVT_BUTTON, self.btn_cancel_order_clicked )
		self.btn_back.Bind( wx.EVT_BUTTON, self.btn_back_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_cancel_order_clicked( self, event ):
		event.Skip()

	def btn_back_onclick( self, event ):
		event.Skip()


###########################################################################
## Class menungguPembayaran
###########################################################################

class menungguPembayaran ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		sbSizer40 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Pesanan Menunggu Pembayaran" ), wx.VERTICAL )

		self.list_order_waiting_payment = wx.ListCtrl( sbSizer40.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		sbSizer40.Add( self.list_order_waiting_payment, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( sbSizer40, 1, wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_back = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.btn_back, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_order_detail = wx.Button( self, wx.ID_ANY, u"Lihat Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_order_detail.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.btn_order_detail.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		gSizer9.Add( self.btn_order_detail, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( gSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.list_order_waiting_payment.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.list_order_waiting_payment_on_list_deselected )
		self.list_order_waiting_payment.Bind( wx.EVT_LIST_ITEM_SELECTED, self.list_order_waiting_payment_on_list_selected )
		self.btn_back.Bind( wx.EVT_BUTTON, self.btn_back_onclick )
		self.btn_order_detail.Bind( wx.EVT_BUTTON, self.btn_order_detail_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def list_order_waiting_payment_on_list_deselected( self, event ):
		event.Skip()

	def list_order_waiting_payment_on_list_selected( self, event ):
		event.Skip()

	def btn_back_onclick( self, event ):
		event.Skip()

	def btn_order_detail_onclick( self, event ):
		event.Skip()


###########################################################################
## Class bayarPesananDetail
###########################################################################

class bayarPesananDetail ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,551 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		sbSizer20 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Kode Booking" ), wx.VERTICAL )

		self.text_kode_booking = wx.TextCtrl( sbSizer20.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer20.Add( self.text_kode_booking, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer20, 1, wx.EXPAND, 5 )

		sbSizer201 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Paket Wisata" ), wx.VERTICAL )

		self.text_paket_wisata = wx.TextCtrl( sbSizer201.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer201.Add( self.text_paket_wisata, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer201, 1, wx.EXPAND, 5 )

		sbSizer202 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tanggal Berangkat" ), wx.VERTICAL )

		self.text_tanggal_berangkat = wx.TextCtrl( sbSizer202.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer202.Add( self.text_tanggal_berangkat, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer202, 1, wx.EXPAND, 5 )

		sbSizer203 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tanggal Pulang" ), wx.VERTICAL )

		self.text_tanggal_pulang = wx.TextCtrl( sbSizer203.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer203.Add( self.text_tanggal_pulang, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer203, 1, wx.EXPAND, 5 )

		sbSizer204 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Status" ), wx.VERTICAL )

		self.text_status = wx.TextCtrl( sbSizer204.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer204.Add( self.text_status, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer204, 1, wx.EXPAND, 5 )

		sbSizer2041 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Nomor Referensi Pembayaran" ), wx.VERTICAL )

		self.text_kode_referensi = wx.TextCtrl( sbSizer2041.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2041.Add( self.text_kode_referensi, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( sbSizer2041, 1, wx.EXPAND, 5 )

		self.btn_bayar = wx.Button( self, wx.ID_ANY, u"Bayar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_bayar.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.btn_bayar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer29.Add( self.btn_bayar, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_back = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.btn_back, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer29 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.text_kode_referensi.Bind( wx.EVT_TEXT, self.text_kode_referensi_onchange )
		self.btn_bayar.Bind( wx.EVT_BUTTON, self.btn_bayar_onclick )
		self.btn_back.Bind( wx.EVT_BUTTON, self.btn_back_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def text_kode_referensi_onchange( self, event ):
		event.Skip()

	def btn_bayar_onclick( self, event ):
		event.Skip()

	def btn_back_onclick( self, event ):
		event.Skip()


