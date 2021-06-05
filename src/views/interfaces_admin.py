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
## Class beranda
###########################################################################

class beranda ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Beranda (Admin) - Aplikasi Wisata", pos = wx.DefaultPosition, size = wx.Size( 500,453 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"BERANDA" ), wx.VERTICAL )

		self.btn_order_waiting_payment_verification = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Order Menunggu Verifikasi Pembayaran", wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		self.btn_order_waiting_payment_verification.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.btn_order_waiting_payment_verification.SetBackgroundColour( wx.Colour( 7, 139, 248 ) )

		sbSizer4.Add( self.btn_order_waiting_payment_verification, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_order_waiting_cancel_verification = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Order Menunggu Verifikasi Pembatalan", wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		self.btn_order_waiting_cancel_verification.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.btn_order_waiting_cancel_verification.SetBackgroundColour( wx.Colour( 0, 0, 160 ) )

		sbSizer4.Add( self.btn_order_waiting_cancel_verification, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_all_order = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Semua Order", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.btn_all_order, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_add_admin = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Tambah Akun Admin", wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		self.btn_add_admin.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.btn_add_admin.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		sbSizer4.Add( self.btn_add_admin, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_logout = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Keluar Akun", wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		self.btn_logout.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.btn_logout.SetBackgroundColour( wx.Colour( 236, 0, 6 ) )

		sbSizer4.Add( self.btn_logout, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( sbSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_order_waiting_payment_verification.Bind( wx.EVT_BUTTON, self.btn_order_waiting_payment_verification_onclick )
		self.btn_order_waiting_cancel_verification.Bind( wx.EVT_BUTTON, self.btn_order_waiting_cancel_verification_onclick )
		self.btn_all_order.Bind( wx.EVT_BUTTON, self.btn_all_order_onclick )
		self.btn_add_admin.Bind( wx.EVT_BUTTON, self.btn_add_admin_onclick )
		self.btn_logout.Bind( wx.EVT_BUTTON, self.btn_logout_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_order_waiting_payment_verification_onclick( self, event ):
		event.Skip()

	def btn_order_waiting_cancel_verification_onclick( self, event ):
		event.Skip()

	def btn_all_order_onclick( self, event ):
		event.Skip()

	def btn_add_admin_onclick( self, event ):
		event.Skip()

	def btn_logout_onclick( self, event ):
		event.Skip()


###########################################################################
## Class listVerifikasiPembayaran
###########################################################################

class listVerifikasiPembayaran ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,306 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		sbSizer40 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Order Menunggu Verifikasi Pembayaran" ), wx.VERTICAL )

		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( sbSizer40.GetStaticBox(), wx.ID_ANY, u"Kode Booking", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer61.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )

		self.text_search = wx.TextCtrl( sbSizer40.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.text_search, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btn_search = wx.Button( sbSizer40.GetStaticBox(), wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.btn_search, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer40.Add( bSizer61, 1, wx.EXPAND, 5 )

		self.list_orders = wx.ListCtrl( sbSizer40.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		sbSizer40.Add( self.list_orders, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( sbSizer40, 1, wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_back = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.btn_back, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_detail = wx.Button( self, wx.ID_ANY, u"Lihat Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_detail.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.btn_detail.SetBackgroundColour( wx.Colour( 67, 95, 203 ) )

		gSizer9.Add( self.btn_detail, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( gSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_search.Bind( wx.EVT_BUTTON, self.btn_search_onclick )
		self.list_orders.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.list_orders_deselected )
		self.list_orders.Bind( wx.EVT_LIST_ITEM_SELECTED, self.list_orders_selected )
		self.btn_back.Bind( wx.EVT_BUTTON, self.btn_back_onclick )
		self.btn_detail.Bind( wx.EVT_BUTTON, self.btn_detail_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_search_onclick( self, event ):
		event.Skip()

	def list_orders_deselected( self, event ):
		event.Skip()

	def list_orders_selected( self, event ):
		event.Skip()

	def btn_back_onclick( self, event ):
		event.Skip()

	def btn_detail_onclick( self, event ):
		event.Skip()


###########################################################################
## Class listVerifikasiPembatalan
###########################################################################

class listVerifikasiPembatalan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,318 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		sbSizer40 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Order Menunggu Verifikasi Pembatalan" ), wx.VERTICAL )

		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( sbSizer40.GetStaticBox(), wx.ID_ANY, u"Kode Booking", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer61.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )

		self.text_search = wx.TextCtrl( sbSizer40.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.text_search, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btn_search = wx.Button( sbSizer40.GetStaticBox(), wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.btn_search, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer40.Add( bSizer61, 1, wx.EXPAND, 5 )

		self.list_orders = wx.ListCtrl( sbSizer40.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		sbSizer40.Add( self.list_orders, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( sbSizer40, 1, wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_back = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.btn_back, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_detail = wx.Button( self, wx.ID_ANY, u"Lihat Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_detail.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.btn_detail.SetBackgroundColour( wx.Colour( 67, 95, 203 ) )

		gSizer9.Add( self.btn_detail, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( gSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_search.Bind( wx.EVT_BUTTON, self.btn_search_onclick )
		self.list_orders.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.list_orders_deselected )
		self.list_orders.Bind( wx.EVT_LIST_ITEM_SELECTED, self.list_orders_selected )
		self.btn_back.Bind( wx.EVT_BUTTON, self.btn_back_onclick )
		self.btn_detail.Bind( wx.EVT_BUTTON, self.btn_detail_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_search_onclick( self, event ):
		event.Skip()

	def list_orders_deselected( self, event ):
		event.Skip()

	def list_orders_selected( self, event ):
		event.Skip()

	def btn_back_onclick( self, event ):
		event.Skip()

	def btn_detail_onclick( self, event ):
		event.Skip()


###########################################################################
## Class listSemuaOrder
###########################################################################

class listSemuaOrder ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		sbSizer40 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Semua Order" ), wx.VERTICAL )

		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( sbSizer40.GetStaticBox(), wx.ID_ANY, u"Kode Booking", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer61.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )

		self.text_search = wx.TextCtrl( sbSizer40.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.text_search, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btn_search = wx.Button( sbSizer40.GetStaticBox(), wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.btn_search, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer40.Add( bSizer61, 1, wx.EXPAND, 5 )

		self.list_orders = wx.ListCtrl( sbSizer40.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		sbSizer40.Add( self.list_orders, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( sbSizer40, 1, wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_back = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.btn_back, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_detail = wx.Button( self, wx.ID_ANY, u"Lihat Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_detail.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.btn_detail.SetBackgroundColour( wx.Colour( 67, 95, 203 ) )

		gSizer9.Add( self.btn_detail, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( gSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_search.Bind( wx.EVT_BUTTON, self.btn_search_onclick )
		self.list_orders.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.list_orders_deselected )
		self.list_orders.Bind( wx.EVT_LIST_ITEM_SELECTED, self.list_orders_selected )
		self.btn_back.Bind( wx.EVT_BUTTON, self.btn_back_onclick )
		self.btn_detail.Bind( wx.EVT_BUTTON, self.btn_detail_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_search_onclick( self, event ):
		event.Skip()

	def list_orders_deselected( self, event ):
		event.Skip()

	def list_orders_selected( self, event ):
		event.Skip()

	def btn_back_onclick( self, event ):
		event.Skip()

	def btn_detail_onclick( self, event ):
		event.Skip()


###########################################################################
## Class detailVerifikasiPembayaran
###########################################################################

class detailVerifikasiPembayaran ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 737,568 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		sbSizer23 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Kode Booking" ), wx.VERTICAL )

		self.txt_kode_booking = wx.TextCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer23.Add( self.txt_kode_booking, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer23, 1, wx.EXPAND, 5 )

		sbSizer234 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Nama Pelanggan" ), wx.VERTICAL )

		self.txt_nama_pelanggan = wx.TextCtrl( sbSizer234.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer234.Add( self.txt_nama_pelanggan, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer234, 1, wx.EXPAND, 5 )

		sbSizer235 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"No. HP Pelanggan" ), wx.VERTICAL )

		self.txt_no_hp = wx.TextCtrl( sbSizer235.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer235.Add( self.txt_no_hp, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer235, 1, wx.EXPAND, 5 )

		sbSizer231 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Paket Wisata" ), wx.VERTICAL )

		self.txt_paket_wisata = wx.TextCtrl( sbSizer231.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer231.Add( self.txt_paket_wisata, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer231, 1, wx.EXPAND, 5 )

		sbSizer232 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tanggal Berangkat" ), wx.VERTICAL )

		self.txt_tanggal_berangkat = wx.TextCtrl( sbSizer232.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer232.Add( self.txt_tanggal_berangkat, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer232, 1, wx.EXPAND, 5 )

		sbSizer2321 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tanggal Pulang" ), wx.VERTICAL )

		self.txt_tanggal_pulang = wx.TextCtrl( sbSizer2321.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer2321.Add( self.txt_tanggal_pulang, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer2321, 1, wx.EXPAND, 5 )

		sbSizer23211 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Status" ), wx.VERTICAL )

		self.txt_status = wx.TextCtrl( sbSizer23211.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer23211.Add( self.txt_status, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer23211, 1, wx.EXPAND, 5 )

		sbSizer233 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Referensi Pembayaran" ), wx.VERTICAL )

		self.txt_referensi_pembayaran = wx.TextCtrl( sbSizer233.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer233.Add( self.txt_referensi_pembayaran, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer233, 1, wx.EXPAND, 5 )


		bSizer17.Add( bSizer18, 1, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		sbSizer24 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Destinasi Wisata" ), wx.VERTICAL )

		self.list_daftar_destinasi = wx.ListCtrl( sbSizer24.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		sbSizer24.Add( self.list_daftar_destinasi, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer19.Add( sbSizer24, 1, wx.EXPAND, 5 )

		sbSizer241 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Peserta" ), wx.VERTICAL )

		self.list_daftar_peserta = wx.ListCtrl( sbSizer241.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		sbSizer241.Add( self.list_daftar_peserta, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer19.Add( sbSizer241, 1, wx.EXPAND, 5 )


		bSizer17.Add( bSizer19, 1, wx.EXPAND, 5 )


		bSizer26.Add( bSizer17, 1, wx.EXPAND, 5 )

		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_back = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.btn_back, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_confirm_payment = wx.Button( self, wx.ID_ANY, u"Konfirmasi Pembayaran", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_confirm_payment.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.btn_confirm_payment.SetBackgroundColour( wx.Colour( 32, 130, 210 ) )

		bSizer28.Add( self.btn_confirm_payment, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer26.Add( bSizer28, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer26 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_back.Bind( wx.EVT_BUTTON, self.btn_back_onclick )
		self.btn_confirm_payment.Bind( wx.EVT_BUTTON, self.btn_confirm_payment_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_back_onclick( self, event ):
		event.Skip()

	def btn_confirm_payment_onclick( self, event ):
		event.Skip()


###########################################################################
## Class daftarAdminBaru
###########################################################################

class daftarAdminBaru ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,346 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		sbSizer27 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Admin Baru" ), wx.VERTICAL )

		sbSizer28 = wx.StaticBoxSizer( wx.StaticBox( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Nama" ), wx.VERTICAL )

		self.text_name = wx.TextCtrl( sbSizer28.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer28.Add( self.text_name, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer27.Add( sbSizer28, 1, wx.EXPAND, 5 )

		sbSizer29 = wx.StaticBoxSizer( wx.StaticBox( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Email" ), wx.VERTICAL )

		self.text_email = wx.TextCtrl( sbSizer29.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer29.Add( self.text_email, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer27.Add( sbSizer29, 1, wx.EXPAND, 5 )

		sbSizer30 = wx.StaticBoxSizer( wx.StaticBox( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Password" ), wx.VERTICAL )

		self.text_password = wx.TextCtrl( sbSizer30.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		sbSizer30.Add( self.text_password, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer27.Add( sbSizer30, 1, wx.EXPAND, 5 )

		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Konfirmasi Password" ), wx.VERTICAL )

		self.text_confirm_password = wx.TextCtrl( sbSizer31.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		sbSizer31.Add( self.text_confirm_password, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer27.Add( sbSizer31, 1, wx.EXPAND, 5 )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_back = wx.Button( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.btn_back, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_register_admin = wx.Button( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Daftar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_register_admin.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_register_admin.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		gSizer10.Add( self.btn_register_admin, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer27.Add( gSizer10, 1, wx.EXPAND, 5 )


		bSizer13.Add( sbSizer27, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_back.Bind( wx.EVT_BUTTON, self.btn_back_onclick )
		self.btn_register_admin.Bind( wx.EVT_BUTTON, self.btn_register_admin_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_back_onclick( self, event ):
		event.Skip()

	def btn_register_admin_onclick( self, event ):
		event.Skip()


###########################################################################
## Class detailVerifikasiPembatalan
###########################################################################

class detailVerifikasiPembatalan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 737,568 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		sbSizer23 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Kode Booking" ), wx.VERTICAL )

		self.txt_kode_booking = wx.TextCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer23.Add( self.txt_kode_booking, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer23, 1, wx.EXPAND, 5 )

		sbSizer234 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Nama Pelanggan" ), wx.VERTICAL )

		self.txt_nama_pelanggan = wx.TextCtrl( sbSizer234.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer234.Add( self.txt_nama_pelanggan, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer234, 1, wx.EXPAND, 5 )

		sbSizer235 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"No. HP Pelanggan" ), wx.VERTICAL )

		self.txt_no_hp = wx.TextCtrl( sbSizer235.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer235.Add( self.txt_no_hp, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer235, 1, wx.EXPAND, 5 )

		sbSizer231 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Paket Wisata" ), wx.VERTICAL )

		self.txt_paket_wisata = wx.TextCtrl( sbSizer231.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer231.Add( self.txt_paket_wisata, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer231, 1, wx.EXPAND, 5 )

		sbSizer232 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tanggal Berangkat" ), wx.VERTICAL )

		self.txt_tanggal_berangkat = wx.TextCtrl( sbSizer232.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer232.Add( self.txt_tanggal_berangkat, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer232, 1, wx.EXPAND, 5 )

		sbSizer2321 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tanggal Pulang" ), wx.VERTICAL )

		self.txt_tanggal_pulang = wx.TextCtrl( sbSizer2321.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer2321.Add( self.txt_tanggal_pulang, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer2321, 1, wx.EXPAND, 5 )

		sbSizer23211 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Status" ), wx.VERTICAL )

		self.txt_status = wx.TextCtrl( sbSizer23211.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer23211.Add( self.txt_status, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer23211, 1, wx.EXPAND, 5 )

		sbSizer233 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Referensi Pembayaran" ), wx.VERTICAL )

		self.txt_referensi_pembayaran = wx.TextCtrl( sbSizer233.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer233.Add( self.txt_referensi_pembayaran, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer233, 1, wx.EXPAND, 5 )


		bSizer17.Add( bSizer18, 1, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		sbSizer24 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Destinasi Wisata" ), wx.VERTICAL )

		self.list_daftar_destinasi = wx.ListCtrl( sbSizer24.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		sbSizer24.Add( self.list_daftar_destinasi, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer19.Add( sbSizer24, 1, wx.EXPAND, 5 )

		sbSizer241 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Peserta" ), wx.VERTICAL )

		self.list_daftar_peserta = wx.ListCtrl( sbSizer241.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		sbSizer241.Add( self.list_daftar_peserta, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer19.Add( sbSizer241, 1, wx.EXPAND, 5 )


		bSizer17.Add( bSizer19, 1, wx.EXPAND, 5 )


		bSizer26.Add( bSizer17, 1, wx.EXPAND, 5 )

		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_back = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.btn_back, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_cancel_order = wx.Button( self, wx.ID_ANY, u"Batalkan Pesanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_cancel_order.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.btn_cancel_order.SetBackgroundColour( wx.Colour( 192, 50, 50 ) )

		bSizer28.Add( self.btn_cancel_order, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer26.Add( bSizer28, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer26 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_back.Bind( wx.EVT_BUTTON, self.btn_back_onclick )
		self.btn_cancel_order.Bind( wx.EVT_BUTTON, self.btn_cancel_order_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_back_onclick( self, event ):
		event.Skip()

	def btn_cancel_order_onclick( self, event ):
		event.Skip()


###########################################################################
## Class detailOrder
###########################################################################

class detailOrder ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 737,568 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		sbSizer23 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Kode Booking" ), wx.VERTICAL )

		self.txt_kode_booking = wx.TextCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer23.Add( self.txt_kode_booking, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer23, 1, wx.EXPAND, 5 )

		sbSizer234 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Nama Pelanggan" ), wx.VERTICAL )

		self.txt_nama_pelanggan = wx.TextCtrl( sbSizer234.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer234.Add( self.txt_nama_pelanggan, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer234, 1, wx.EXPAND, 5 )

		sbSizer235 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"No. HP Pelanggan" ), wx.VERTICAL )

		self.txt_no_hp = wx.TextCtrl( sbSizer235.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer235.Add( self.txt_no_hp, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer235, 1, wx.EXPAND, 5 )

		sbSizer231 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Paket Wisata" ), wx.VERTICAL )

		self.txt_paket_wisata = wx.TextCtrl( sbSizer231.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer231.Add( self.txt_paket_wisata, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer231, 1, wx.EXPAND, 5 )

		sbSizer232 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tanggal Berangkat" ), wx.VERTICAL )

		self.txt_tanggal_berangkat = wx.TextCtrl( sbSizer232.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer232.Add( self.txt_tanggal_berangkat, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer232, 1, wx.EXPAND, 5 )

		sbSizer2321 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tanggal Pulang" ), wx.VERTICAL )

		self.txt_tanggal_pulang = wx.TextCtrl( sbSizer2321.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer2321.Add( self.txt_tanggal_pulang, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer2321, 1, wx.EXPAND, 5 )

		sbSizer23211 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Status" ), wx.VERTICAL )

		self.txt_status = wx.TextCtrl( sbSizer23211.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer23211.Add( self.txt_status, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer23211, 1, wx.EXPAND, 5 )

		sbSizer233 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Referensi Pembayaran" ), wx.VERTICAL )

		self.txt_referensi_pembayaran = wx.TextCtrl( sbSizer233.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer233.Add( self.txt_referensi_pembayaran, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( sbSizer233, 1, wx.EXPAND, 5 )


		bSizer17.Add( bSizer18, 1, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		sbSizer24 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Destinasi Wisata" ), wx.VERTICAL )

		self.list_daftar_destinasi = wx.ListCtrl( sbSizer24.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		sbSizer24.Add( self.list_daftar_destinasi, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer19.Add( sbSizer24, 1, wx.EXPAND, 5 )

		sbSizer241 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Peserta" ), wx.VERTICAL )

		self.list_daftar_peserta = wx.ListCtrl( sbSizer241.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		sbSizer241.Add( self.list_daftar_peserta, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer19.Add( sbSizer241, 1, wx.EXPAND, 5 )


		bSizer17.Add( bSizer19, 1, wx.EXPAND, 5 )


		bSizer26.Add( bSizer17, 1, wx.EXPAND, 5 )

		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_back = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.btn_back, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer28.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer26.Add( bSizer28, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer26 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_back.Bind( wx.EVT_BUTTON, self.btn_back_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_back_onclick( self, event ):
		event.Skip()


