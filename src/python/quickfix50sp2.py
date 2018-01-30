import quickfix as fix

class Message(fix.Message):
	def __init__(self):
		fix.Message.__init__(self)
		self.getHeader().setField( fix.BeginString("FIXT.1.1") )
		self.getHeader().setField( fix.ApplVerID("9") )

class IOI(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("6") )

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(58)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 682
			order[56] = 683
			order[57] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

		class NoLegStipulations(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 688
				order[1] = 689
				order[2] = 0
				fix.Group.__init__(self, 683, 688, order)

	class NoIOIQualifiers(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 104
			order[1] = 0
			fix.Group.__init__(self, 199, 104, order)

	class NoRoutingIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 216
			order[1] = 217
			order[2] = 0
			fix.Group.__init__(self, 215, 216, order)

class Advertisement(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("7") )

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

class ExecutionReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("8") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoContraBrokers(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 375
			order[1] = 337
			order[2] = 437
			order[3] = 438
			order[4] = 655
			order[5] = 0
			fix.Group.__init__(self, 382, 375, order)

	class NoAllocs(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 79
			order[1] = 661
			order[2] = 736
			order[3] = 467
			order[4] = 539
			order[5] = 80
			order[6] = 0
			fix.Group.__init__(self, 78, 79, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoStrategyParameters(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 958
			order[1] = 959
			order[2] = 960
			order[3] = 0
			fix.Group.__init__(self, 957, 958, order)

	class NoFills(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 1363
			order[1] = 1364
			order[2] = 1365
			order[3] = 1414
			order[4] = 1443
			order[5] = 0
			fix.Group.__init__(self, 1362, 1363, order)

		class NoNested4PartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1415
				order[1] = 1416
				order[2] = 1417
				order[3] = 1413
				order[4] = 0
				fix.Group.__init__(self, 1414, 1415, order)

			class NoNested4PartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1412
					order[1] = 1411
					order[2] = 0
					fix.Group.__init__(self, 1413, 1412, order)

	class NoContAmts(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 519
			order[1] = 520
			order[2] = 521
			order[3] = 0
			fix.Group.__init__(self, 518, 519, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(78)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 687
			order[56] = 685
			order[57] = 690
			order[58] = 683
			order[59] = 1366
			order[60] = 670
			order[61] = 564
			order[62] = 565
			order[63] = 948
			order[64] = 654
			order[65] = 587
			order[66] = 588
			order[67] = 637
			order[68] = 675
			order[69] = 1073
			order[70] = 1074
			order[71] = 1075
			order[72] = 1379
			order[73] = 1381
			order[74] = 1383
			order[75] = 1384
			order[76] = 1418
			order[77] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

		class NoLegStipulations(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 688
				order[1] = 689
				order[2] = 0
				fix.Group.__init__(self, 683, 688, order)

		class NoLegAllocs(fix.Group):
			def __init__(self):
				order = fix.IntArray(7)
				order[0] = 671
				order[1] = 672
				order[2] = 756
				order[3] = 673
				order[4] = 674
				order[5] = 1367
				order[6] = 0
				fix.Group.__init__(self, 670, 671, order)

			class NoNested2PartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 757
					order[1] = 758
					order[2] = 759
					order[3] = 806
					order[4] = 0
					fix.Group.__init__(self, 756, 757, order)

				class NoNested2PartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 760
						order[1] = 807
						order[2] = 0
						fix.Group.__init__(self, 806, 760, order)

		class NoNested3PartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 949
				order[1] = 950
				order[2] = 951
				order[3] = 952
				order[4] = 0
				fix.Group.__init__(self, 948, 949, order)

			class NoNested3PartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 953
					order[1] = 954
					order[2] = 0
					fix.Group.__init__(self, 952, 953, order)

	class NoMiscFees(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 137
			order[1] = 138
			order[2] = 139
			order[3] = 891
			order[4] = 0
			fix.Group.__init__(self, 136, 137, order)

	class NoTrdRegTimestamps(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 769
			order[1] = 770
			order[2] = 771
			order[3] = 1033
			order[4] = 1034
			order[5] = 1035
			order[6] = 0
			fix.Group.__init__(self, 768, 769, order)

	class NoRateSources(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1446
			order[1] = 1447
			order[2] = 1448
			order[3] = 0
			fix.Group.__init__(self, 1445, 1446, order)

class OrderCancelReject(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("9") )

class News(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("B") )

	class NoRoutingIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 216
			order[1] = 217
			order[2] = 0
			fix.Group.__init__(self, 215, 216, order)

	class NoRelatedSym(fix.Group):
		def __init__(self):
			order = fix.IntArray(82)
			order[0] = 55
			order[1] = 65
			order[2] = 48
			order[3] = 22
			order[4] = 460
			order[5] = 1227
			order[6] = 1151
			order[7] = 461
			order[8] = 167
			order[9] = 762
			order[10] = 200
			order[11] = 541
			order[12] = 1079
			order[13] = 966
			order[14] = 1049
			order[15] = 965
			order[16] = 224
			order[17] = 225
			order[18] = 239
			order[19] = 226
			order[20] = 227
			order[21] = 228
			order[22] = 255
			order[23] = 543
			order[24] = 470
			order[25] = 471
			order[26] = 472
			order[27] = 240
			order[28] = 202
			order[29] = 947
			order[30] = 967
			order[31] = 968
			order[32] = 206
			order[33] = 231
			order[34] = 969
			order[35] = 1146
			order[36] = 996
			order[37] = 1147
			order[38] = 1191
			order[39] = 1192
			order[40] = 1193
			order[41] = 1194
			order[42] = 1195
			order[43] = 1196
			order[44] = 1197
			order[45] = 1198
			order[46] = 1199
			order[47] = 1200
			order[48] = 201
			order[49] = 1244
			order[50] = 1242
			order[51] = 997
			order[52] = 223
			order[53] = 207
			order[54] = 970
			order[55] = 971
			order[56] = 106
			order[57] = 348
			order[58] = 349
			order[59] = 107
			order[60] = 350
			order[61] = 351
			order[62] = 691
			order[63] = 667
			order[64] = 875
			order[65] = 876
			order[66] = 873
			order[67] = 874
			order[68] = 1435
			order[69] = 1439
			order[70] = 1449
			order[71] = 1450
			order[72] = 1451
			order[73] = 1452
			order[74] = 1457
			order[75] = 1458
			order[76] = 1478
			order[77] = 1479
			order[78] = 1480
			order[79] = 1481
			order[80] = 1482
			order[81] = 0
			fix.Group.__init__(self, 146, 55, order)

		class NoSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 455
				order[1] = 456
				order[2] = 0
				fix.Group.__init__(self, 454, 455, order)

		class NoEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 865
				order[1] = 866
				order[2] = 1145
				order[3] = 867
				order[4] = 868
				order[5] = 0
				fix.Group.__init__(self, 864, 865, order)

		class NoInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1019
				order[1] = 1050
				order[2] = 1051
				order[3] = 1052
				order[4] = 0
				fix.Group.__init__(self, 1018, 1019, order)

			class NoInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1053
					order[1] = 1054
					order[2] = 0
					fix.Group.__init__(self, 1052, 1053, order)

		class NoComplexEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(9)
				order[0] = 1484
				order[1] = 1485
				order[2] = 1486
				order[3] = 1487
				order[4] = 1488
				order[5] = 1489
				order[6] = 1490
				order[7] = 1491
				order[8] = 0
				fix.Group.__init__(self, 1483, 1484, order)

			class NoComplexEventDates(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1492
					order[1] = 1493
					order[2] = 1494
					order[3] = 0
					fix.Group.__init__(self, 1491, 1492, order)

				class NoComplexEventTimes(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1495
						order[1] = 1496
						order[2] = 0
						fix.Group.__init__(self, 1494, 1495, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLinesOfText(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 58
			order[1] = 354
			order[2] = 355
			order[3] = 0
			fix.Group.__init__(self, 33, 58, order)

	class NoNewsRefIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 1476
			order[1] = 1477
			order[2] = 0
			fix.Group.__init__(self, 1475, 1476, order)

class Email(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("C") )

	class NoRoutingIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 216
			order[1] = 217
			order[2] = 0
			fix.Group.__init__(self, 215, 216, order)

	class NoRelatedSym(fix.Group):
		def __init__(self):
			order = fix.IntArray(82)
			order[0] = 55
			order[1] = 65
			order[2] = 48
			order[3] = 22
			order[4] = 460
			order[5] = 1227
			order[6] = 1151
			order[7] = 461
			order[8] = 167
			order[9] = 762
			order[10] = 200
			order[11] = 541
			order[12] = 1079
			order[13] = 966
			order[14] = 1049
			order[15] = 965
			order[16] = 224
			order[17] = 225
			order[18] = 239
			order[19] = 226
			order[20] = 227
			order[21] = 228
			order[22] = 255
			order[23] = 543
			order[24] = 470
			order[25] = 471
			order[26] = 472
			order[27] = 240
			order[28] = 202
			order[29] = 947
			order[30] = 967
			order[31] = 968
			order[32] = 206
			order[33] = 231
			order[34] = 969
			order[35] = 1146
			order[36] = 996
			order[37] = 1147
			order[38] = 1191
			order[39] = 1192
			order[40] = 1193
			order[41] = 1194
			order[42] = 1195
			order[43] = 1196
			order[44] = 1197
			order[45] = 1198
			order[46] = 1199
			order[47] = 1200
			order[48] = 201
			order[49] = 1244
			order[50] = 1242
			order[51] = 997
			order[52] = 223
			order[53] = 207
			order[54] = 970
			order[55] = 971
			order[56] = 106
			order[57] = 348
			order[58] = 349
			order[59] = 107
			order[60] = 350
			order[61] = 351
			order[62] = 691
			order[63] = 667
			order[64] = 875
			order[65] = 876
			order[66] = 873
			order[67] = 874
			order[68] = 1435
			order[69] = 1439
			order[70] = 1449
			order[71] = 1450
			order[72] = 1451
			order[73] = 1452
			order[74] = 1457
			order[75] = 1458
			order[76] = 1478
			order[77] = 1479
			order[78] = 1480
			order[79] = 1481
			order[80] = 1482
			order[81] = 0
			fix.Group.__init__(self, 146, 55, order)

		class NoSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 455
				order[1] = 456
				order[2] = 0
				fix.Group.__init__(self, 454, 455, order)

		class NoEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 865
				order[1] = 866
				order[2] = 1145
				order[3] = 867
				order[4] = 868
				order[5] = 0
				fix.Group.__init__(self, 864, 865, order)

		class NoInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1019
				order[1] = 1050
				order[2] = 1051
				order[3] = 1052
				order[4] = 0
				fix.Group.__init__(self, 1018, 1019, order)

			class NoInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1053
					order[1] = 1054
					order[2] = 0
					fix.Group.__init__(self, 1052, 1053, order)

		class NoComplexEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(9)
				order[0] = 1484
				order[1] = 1485
				order[2] = 1486
				order[3] = 1487
				order[4] = 1488
				order[5] = 1489
				order[6] = 1490
				order[7] = 1491
				order[8] = 0
				fix.Group.__init__(self, 1483, 1484, order)

			class NoComplexEventDates(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1492
					order[1] = 1493
					order[2] = 1494
					order[3] = 0
					fix.Group.__init__(self, 1491, 1492, order)

				class NoComplexEventTimes(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1495
						order[1] = 1496
						order[2] = 0
						fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoLinesOfText(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 58
			order[1] = 354
			order[2] = 355
			order[3] = 0
			fix.Group.__init__(self, 33, 58, order)

class NewOrderSingle(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("D") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoAllocs(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 79
			order[1] = 661
			order[2] = 736
			order[3] = 467
			order[4] = 539
			order[5] = 80
			order[6] = 0
			fix.Group.__init__(self, 78, 79, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

	class NoTradingSessions(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 336
			order[1] = 625
			order[2] = 0
			fix.Group.__init__(self, 386, 336, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoStrategyParameters(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 958
			order[1] = 959
			order[2] = 960
			order[3] = 0
			fix.Group.__init__(self, 957, 958, order)

	class NoTrdRegTimestamps(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 769
			order[1] = 770
			order[2] = 771
			order[3] = 1033
			order[4] = 1034
			order[5] = 1035
			order[6] = 0
			fix.Group.__init__(self, 768, 769, order)

class NewOrderList(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("E") )

	class NoRootPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1117
			order[1] = 1118
			order[2] = 1119
			order[3] = 1120
			order[4] = 0
			fix.Group.__init__(self, 1116, 1117, order)

		class NoRootPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1121
				order[1] = 1122
				order[2] = 0
				fix.Group.__init__(self, 1120, 1121, order)

	class NoOrders(fix.Group):
		def __init__(self):
			order = fix.IntArray(223)
			order[0] = 11
			order[1] = 526
			order[2] = 67
			order[3] = 583
			order[4] = 160
			order[5] = 453
			order[6] = 229
			order[7] = 75
			order[8] = 1
			order[9] = 660
			order[10] = 581
			order[11] = 589
			order[12] = 590
			order[13] = 70
			order[14] = 591
			order[15] = 78
			order[16] = 63
			order[17] = 64
			order[18] = 544
			order[19] = 635
			order[20] = 21
			order[21] = 18
			order[22] = 110
			order[23] = 1089
			order[24] = 1090
			order[25] = 1138
			order[26] = 1082
			order[27] = 1083
			order[28] = 1084
			order[29] = 1085
			order[30] = 1086
			order[31] = 1087
			order[32] = 1088
			order[33] = 111
			order[34] = 100
			order[35] = 1133
			order[36] = 386
			order[37] = 81
			order[38] = 55
			order[39] = 65
			order[40] = 48
			order[41] = 22
			order[42] = 460
			order[43] = 1227
			order[44] = 1151
			order[45] = 461
			order[46] = 167
			order[47] = 762
			order[48] = 200
			order[49] = 541
			order[50] = 1079
			order[51] = 966
			order[52] = 1049
			order[53] = 965
			order[54] = 224
			order[55] = 225
			order[56] = 239
			order[57] = 226
			order[58] = 227
			order[59] = 228
			order[60] = 255
			order[61] = 543
			order[62] = 470
			order[63] = 471
			order[64] = 472
			order[65] = 240
			order[66] = 202
			order[67] = 947
			order[68] = 967
			order[69] = 968
			order[70] = 206
			order[71] = 231
			order[72] = 969
			order[73] = 1146
			order[74] = 996
			order[75] = 1147
			order[76] = 1191
			order[77] = 1192
			order[78] = 1193
			order[79] = 1194
			order[80] = 1195
			order[81] = 1196
			order[82] = 1197
			order[83] = 1198
			order[84] = 1199
			order[85] = 1200
			order[86] = 201
			order[87] = 1244
			order[88] = 1242
			order[89] = 997
			order[90] = 223
			order[91] = 207
			order[92] = 970
			order[93] = 971
			order[94] = 106
			order[95] = 348
			order[96] = 349
			order[97] = 107
			order[98] = 350
			order[99] = 351
			order[100] = 691
			order[101] = 667
			order[102] = 875
			order[103] = 876
			order[104] = 873
			order[105] = 874
			order[106] = 1435
			order[107] = 1439
			order[108] = 1449
			order[109] = 1450
			order[110] = 1451
			order[111] = 1452
			order[112] = 1457
			order[113] = 1458
			order[114] = 1478
			order[115] = 1479
			order[116] = 1480
			order[117] = 1481
			order[118] = 1482
			order[119] = 711
			order[120] = 140
			order[121] = 54
			order[122] = 401
			order[123] = 114
			order[124] = 60
			order[125] = 232
			order[126] = 854
			order[127] = 38
			order[128] = 152
			order[129] = 516
			order[130] = 468
			order[131] = 469
			order[132] = 40
			order[133] = 423
			order[134] = 44
			order[135] = 1092
			order[136] = 99
			order[137] = 1100
			order[138] = 1101
			order[139] = 1102
			order[140] = 1103
			order[141] = 1104
			order[142] = 1105
			order[143] = 1106
			order[144] = 1107
			order[145] = 1108
			order[146] = 1109
			order[147] = 1110
			order[148] = 1111
			order[149] = 1112
			order[150] = 1113
			order[151] = 1114
			order[152] = 218
			order[153] = 22048
			order[154] = 220
			order[155] = 221
			order[156] = 222
			order[157] = 662
			order[158] = 663
			order[159] = 699
			order[160] = 761
			order[161] = 235
			order[162] = 236
			order[163] = 701
			order[164] = 696
			order[165] = 697
			order[166] = 698
			order[167] = 15
			order[168] = 376
			order[169] = 377
			order[170] = 23
			order[171] = 117
			order[172] = 1080
			order[173] = 1081
			order[174] = 59
			order[175] = 168
			order[176] = 432
			order[177] = 126
			order[178] = 427
			order[179] = 12
			order[180] = 13
			order[181] = 479
			order[182] = 497
			order[183] = 528
			order[184] = 529
			order[185] = 1091
			order[186] = 582
			order[187] = 121
			order[188] = 120
			order[189] = 775
			order[190] = 58
			order[191] = 354
			order[192] = 355
			order[193] = 193
			order[194] = 192
			order[195] = 640
			order[196] = 77
			order[197] = 203
			order[198] = 210
			order[199] = 211
			order[200] = 1094
			order[201] = 835
			order[202] = 836
			order[203] = 837
			order[204] = 838
			order[205] = 840
			order[206] = 1096
			order[207] = 1097
			order[208] = 1098
			order[209] = 1099
			order[210] = 388
			order[211] = 389
			order[212] = 841
			order[213] = 842
			order[214] = 843
			order[215] = 844
			order[216] = 846
			order[217] = 847
			order[218] = 957
			order[219] = 848
			order[220] = 849
			order[221] = 494
			order[222] = 0
			fix.Group.__init__(self, 73, 11, order)

		class NoPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 448
				order[1] = 447
				order[2] = 452
				order[3] = 2376
				order[4] = 802
				order[5] = 0
				fix.Group.__init__(self, 453, 448, order)

			class NoPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 523
					order[1] = 803
					order[2] = 0
					fix.Group.__init__(self, 802, 523, order)

		class NoAllocs(fix.Group):
			def __init__(self):
				order = fix.IntArray(7)
				order[0] = 79
				order[1] = 661
				order[2] = 736
				order[3] = 467
				order[4] = 539
				order[5] = 80
				order[6] = 0
				fix.Group.__init__(self, 78, 79, order)

			class NoNestedPartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 524
					order[1] = 525
					order[2] = 538
					order[3] = 804
					order[4] = 0
					fix.Group.__init__(self, 539, 524, order)

				class NoNestedPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 545
						order[1] = 805
						order[2] = 0
						fix.Group.__init__(self, 804, 545, order)

		class NoTradingSessions(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 336
				order[1] = 625
				order[2] = 0
				fix.Group.__init__(self, 386, 336, order)

		class NoSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 455
				order[1] = 456
				order[2] = 0
				fix.Group.__init__(self, 454, 455, order)

		class NoEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 865
				order[1] = 866
				order[2] = 1145
				order[3] = 867
				order[4] = 868
				order[5] = 0
				fix.Group.__init__(self, 864, 865, order)

		class NoInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1019
				order[1] = 1050
				order[2] = 1051
				order[3] = 1052
				order[4] = 0
				fix.Group.__init__(self, 1018, 1019, order)

			class NoInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1053
					order[1] = 1054
					order[2] = 0
					fix.Group.__init__(self, 1052, 1053, order)

		class NoComplexEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(9)
				order[0] = 1484
				order[1] = 1485
				order[2] = 1486
				order[3] = 1487
				order[4] = 1488
				order[5] = 1489
				order[6] = 1490
				order[7] = 1491
				order[8] = 0
				fix.Group.__init__(self, 1483, 1484, order)

			class NoComplexEventDates(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1492
					order[1] = 1493
					order[2] = 1494
					order[3] = 0
					fix.Group.__init__(self, 1491, 1492, order)

				class NoComplexEventTimes(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1495
						order[1] = 1496
						order[2] = 0
						fix.Group.__init__(self, 1494, 1495, order)

		class NoUnderlyings(fix.Group):
			def __init__(self):
				order = fix.IntArray(70)
				order[0] = 311
				order[1] = 312
				order[2] = 309
				order[3] = 305
				order[4] = 462
				order[5] = 463
				order[6] = 310
				order[7] = 763
				order[8] = 313
				order[9] = 542
				order[10] = 1213
				order[11] = 241
				order[12] = 242
				order[13] = 243
				order[14] = 244
				order[15] = 245
				order[16] = 246
				order[17] = 256
				order[18] = 595
				order[19] = 592
				order[20] = 593
				order[21] = 594
				order[22] = 247
				order[23] = 316
				order[24] = 941
				order[25] = 317
				order[26] = 436
				order[27] = 998
				order[28] = 1423
				order[29] = 1424
				order[30] = 1425
				order[31] = 1000
				order[32] = 1419
				order[33] = 435
				order[34] = 308
				order[35] = 306
				order[36] = 362
				order[37] = 363
				order[38] = 307
				order[39] = 364
				order[40] = 365
				order[41] = 877
				order[42] = 878
				order[43] = 972
				order[44] = 318
				order[45] = 879
				order[46] = 975
				order[47] = 973
				order[48] = 974
				order[49] = 810
				order[50] = 882
				order[51] = 883
				order[52] = 884
				order[53] = 885
				order[54] = 886
				order[55] = 1044
				order[56] = 1045
				order[57] = 1046
				order[58] = 1038
				order[59] = 1039
				order[60] = 315
				order[61] = 1437
				order[62] = 1441
				order[63] = 1453
				order[64] = 1454
				order[65] = 1455
				order[66] = 1456
				order[67] = 1459
				order[68] = 1460
				order[69] = 0
				fix.Group.__init__(self, 711, 311, order)

			class NoUnderlyingSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 458
					order[1] = 459
					order[2] = 0
					fix.Group.__init__(self, 457, 458, order)

			class NoUnderlyingStips(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 888
					order[1] = 889
					order[2] = 0
					fix.Group.__init__(self, 887, 888, order)

			class NoUndlyInstrumentParties(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 1059
					order[1] = 1060
					order[2] = 1061
					order[3] = 1062
					order[4] = 0
					fix.Group.__init__(self, 1058, 1059, order)

				class NoUndlyInstrumentPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1063
						order[1] = 1064
						order[2] = 0
						fix.Group.__init__(self, 1062, 1063, order)

		class NoStipulations(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 233
				order[1] = 234
				order[2] = 0
				fix.Group.__init__(self, 232, 233, order)

		class NoStrategyParameters(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 958
				order[1] = 959
				order[2] = 960
				order[3] = 0
				fix.Group.__init__(self, 957, 958, order)

class OrderCancelRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("F") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

class OrderCancelReplaceRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("G") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoAllocs(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 79
			order[1] = 661
			order[2] = 736
			order[3] = 467
			order[4] = 539
			order[5] = 80
			order[6] = 0
			fix.Group.__init__(self, 78, 79, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

	class NoTradingSessions(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 336
			order[1] = 625
			order[2] = 0
			fix.Group.__init__(self, 386, 336, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoStrategyParameters(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 958
			order[1] = 959
			order[2] = 960
			order[3] = 0
			fix.Group.__init__(self, 957, 958, order)

	class NoTrdRegTimestamps(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 769
			order[1] = 770
			order[2] = 771
			order[3] = 1033
			order[4] = 1034
			order[5] = 1035
			order[6] = 0
			fix.Group.__init__(self, 768, 769, order)

class OrderStatusRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("H") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

class AllocationInstruction(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("J") )

	class NoOrders(fix.Group):
		def __init__(self):
			order = fix.IntArray(10)
			order[0] = 11
			order[1] = 37
			order[2] = 198
			order[3] = 526
			order[4] = 66
			order[5] = 756
			order[6] = 38
			order[7] = 799
			order[8] = 800
			order[9] = 0
			fix.Group.__init__(self, 73, 11, order)

		class NoNested2PartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 757
				order[1] = 758
				order[2] = 759
				order[3] = 806
				order[4] = 0
				fix.Group.__init__(self, 756, 757, order)

			class NoNested2PartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 760
					order[1] = 807
					order[2] = 0
					fix.Group.__init__(self, 806, 760, order)

	class NoExecs(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 32
			order[1] = 17
			order[2] = 527
			order[3] = 31
			order[4] = 669
			order[5] = 29
			order[6] = 1003
			order[7] = 1041
			order[8] = 0
			fix.Group.__init__(self, 124, 32, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoInstrAttrib(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 871
			order[1] = 872
			order[2] = 0
			fix.Group.__init__(self, 870, 871, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoPosAmt(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 707
			order[1] = 708
			order[2] = 1055
			order[3] = 0
			fix.Group.__init__(self, 753, 707, order)

	class NoAllocs(fix.Group):
		def __init__(self):
			order = fix.IntArray(41)
			order[0] = 79
			order[1] = 661
			order[2] = 573
			order[3] = 366
			order[4] = 80
			order[5] = 467
			order[6] = 81
			order[7] = 989
			order[8] = 1002
			order[9] = 993
			order[10] = 1047
			order[11] = 992
			order[12] = 539
			order[13] = 208
			order[14] = 209
			order[15] = 161
			order[16] = 360
			order[17] = 361
			order[18] = 12
			order[19] = 13
			order[20] = 479
			order[21] = 497
			order[22] = 153
			order[23] = 154
			order[24] = 119
			order[25] = 737
			order[26] = 120
			order[27] = 736
			order[28] = 155
			order[29] = 156
			order[30] = 742
			order[31] = 741
			order[32] = 136
			order[33] = 576
			order[34] = 635
			order[35] = 780
			order[36] = 172
			order[37] = 169
			order[38] = 170
			order[39] = 171
			order[40] = 0
			fix.Group.__init__(self, 78, 79, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

		class NoMiscFees(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 137
				order[1] = 138
				order[2] = 139
				order[3] = 891
				order[4] = 0
				fix.Group.__init__(self, 136, 137, order)

		class NoClearingInstructions(fix.Group):
			def __init__(self):
				order = fix.IntArray(2)
				order[0] = 577
				order[1] = 0
				fix.Group.__init__(self, 576, 577, order)

		class NoDlvyInst(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 165
				order[1] = 787
				order[2] = 781
				order[3] = 0
				fix.Group.__init__(self, 85, 165, order)

			class NoSettlPartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 782
					order[1] = 783
					order[2] = 784
					order[3] = 801
					order[4] = 0
					fix.Group.__init__(self, 781, 782, order)

				class NoSettlPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 785
						order[1] = 786
						order[2] = 0
						fix.Group.__init__(self, 801, 785, order)

	class NoRateSources(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1446
			order[1] = 1447
			order[2] = 1448
			order[3] = 0
			fix.Group.__init__(self, 1445, 1446, order)

class ListCancelRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("K") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

class ListExecute(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("L") )

class ListStatusRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("M") )

class ListStatus(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("N") )

	class NoOrders(fix.Group):
		def __init__(self):
			order = fix.IntArray(14)
			order[0] = 11
			order[1] = 37
			order[2] = 526
			order[3] = 14
			order[4] = 39
			order[5] = 636
			order[6] = 151
			order[7] = 84
			order[8] = 6
			order[9] = 103
			order[10] = 58
			order[11] = 354
			order[12] = 355
			order[13] = 0
			fix.Group.__init__(self, 73, 11, order)

class AllocationInstructionAck(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("P") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoAllocs(fix.Group):
		def __init__(self):
			order = fix.IntArray(15)
			order[0] = 79
			order[1] = 661
			order[2] = 366
			order[3] = 1047
			order[4] = 467
			order[5] = 776
			order[6] = 539
			order[7] = 161
			order[8] = 360
			order[9] = 361
			order[10] = 989
			order[11] = 993
			order[12] = 992
			order[13] = 80
			order[14] = 0
			fix.Group.__init__(self, 78, 79, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

class DontKnowTrade(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("Q") )

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

class QuoteRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("R") )

	class NoRootPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1117
			order[1] = 1118
			order[2] = 1119
			order[3] = 1120
			order[4] = 0
			fix.Group.__init__(self, 1116, 1117, order)

		class NoRootPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1121
				order[1] = 1122
				order[2] = 0
				fix.Group.__init__(self, 1120, 1121, order)

	class NoRelatedSym(fix.Group):
		def __init__(self):
			order = fix.IntArray(143)
			order[0] = 55
			order[1] = 65
			order[2] = 48
			order[3] = 22
			order[4] = 460
			order[5] = 1227
			order[6] = 1151
			order[7] = 461
			order[8] = 167
			order[9] = 762
			order[10] = 200
			order[11] = 541
			order[12] = 1079
			order[13] = 966
			order[14] = 1049
			order[15] = 965
			order[16] = 224
			order[17] = 225
			order[18] = 239
			order[19] = 226
			order[20] = 227
			order[21] = 228
			order[22] = 255
			order[23] = 543
			order[24] = 470
			order[25] = 471
			order[26] = 472
			order[27] = 240
			order[28] = 202
			order[29] = 947
			order[30] = 967
			order[31] = 968
			order[32] = 206
			order[33] = 231
			order[34] = 969
			order[35] = 1146
			order[36] = 996
			order[37] = 1147
			order[38] = 1191
			order[39] = 1192
			order[40] = 1193
			order[41] = 1194
			order[42] = 1195
			order[43] = 1196
			order[44] = 1197
			order[45] = 1198
			order[46] = 1199
			order[47] = 1200
			order[48] = 201
			order[49] = 1244
			order[50] = 1242
			order[51] = 997
			order[52] = 223
			order[53] = 207
			order[54] = 970
			order[55] = 971
			order[56] = 106
			order[57] = 348
			order[58] = 349
			order[59] = 107
			order[60] = 350
			order[61] = 351
			order[62] = 691
			order[63] = 667
			order[64] = 875
			order[65] = 876
			order[66] = 873
			order[67] = 874
			order[68] = 1435
			order[69] = 1439
			order[70] = 1449
			order[71] = 1450
			order[72] = 1451
			order[73] = 1452
			order[74] = 1457
			order[75] = 1458
			order[76] = 1478
			order[77] = 1479
			order[78] = 1480
			order[79] = 1481
			order[80] = 1482
			order[81] = 913
			order[82] = 914
			order[83] = 915
			order[84] = 918
			order[85] = 788
			order[86] = 916
			order[87] = 917
			order[88] = 919
			order[89] = 898
			order[90] = 711
			order[91] = 140
			order[92] = 303
			order[93] = 537
			order[94] = 336
			order[95] = 625
			order[96] = 229
			order[97] = 54
			order[98] = 854
			order[99] = 38
			order[100] = 152
			order[101] = 516
			order[102] = 468
			order[103] = 469
			order[104] = 110
			order[105] = 63
			order[106] = 64
			order[107] = 193
			order[108] = 192
			order[109] = 15
			order[110] = 232
			order[111] = 1
			order[112] = 660
			order[113] = 581
			order[114] = 555
			order[115] = 735
			order[116] = 692
			order[117] = 40
			order[118] = 62
			order[119] = 126
			order[120] = 60
			order[121] = 218
			order[122] = 22048
			order[123] = 220
			order[124] = 221
			order[125] = 222
			order[126] = 662
			order[127] = 663
			order[128] = 699
			order[129] = 761
			order[130] = 423
			order[131] = 44
			order[132] = 640
			order[133] = 235
			order[134] = 236
			order[135] = 701
			order[136] = 696
			order[137] = 697
			order[138] = 698
			order[139] = 453
			order[140] = 120
			order[141] = 1445
			order[142] = 0
			fix.Group.__init__(self, 146, 55, order)

		class NoSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 455
				order[1] = 456
				order[2] = 0
				fix.Group.__init__(self, 454, 455, order)

		class NoEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 865
				order[1] = 866
				order[2] = 1145
				order[3] = 867
				order[4] = 868
				order[5] = 0
				fix.Group.__init__(self, 864, 865, order)

		class NoInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1019
				order[1] = 1050
				order[2] = 1051
				order[3] = 1052
				order[4] = 0
				fix.Group.__init__(self, 1018, 1019, order)

			class NoInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1053
					order[1] = 1054
					order[2] = 0
					fix.Group.__init__(self, 1052, 1053, order)

		class NoComplexEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(9)
				order[0] = 1484
				order[1] = 1485
				order[2] = 1486
				order[3] = 1487
				order[4] = 1488
				order[5] = 1489
				order[6] = 1490
				order[7] = 1491
				order[8] = 0
				fix.Group.__init__(self, 1483, 1484, order)

			class NoComplexEventDates(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1492
					order[1] = 1493
					order[2] = 1494
					order[3] = 0
					fix.Group.__init__(self, 1491, 1492, order)

				class NoComplexEventTimes(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1495
						order[1] = 1496
						order[2] = 0
						fix.Group.__init__(self, 1494, 1495, order)

		class NoUnderlyings(fix.Group):
			def __init__(self):
				order = fix.IntArray(70)
				order[0] = 311
				order[1] = 312
				order[2] = 309
				order[3] = 305
				order[4] = 462
				order[5] = 463
				order[6] = 310
				order[7] = 763
				order[8] = 313
				order[9] = 542
				order[10] = 1213
				order[11] = 241
				order[12] = 242
				order[13] = 243
				order[14] = 244
				order[15] = 245
				order[16] = 246
				order[17] = 256
				order[18] = 595
				order[19] = 592
				order[20] = 593
				order[21] = 594
				order[22] = 247
				order[23] = 316
				order[24] = 941
				order[25] = 317
				order[26] = 436
				order[27] = 998
				order[28] = 1423
				order[29] = 1424
				order[30] = 1425
				order[31] = 1000
				order[32] = 1419
				order[33] = 435
				order[34] = 308
				order[35] = 306
				order[36] = 362
				order[37] = 363
				order[38] = 307
				order[39] = 364
				order[40] = 365
				order[41] = 877
				order[42] = 878
				order[43] = 972
				order[44] = 318
				order[45] = 879
				order[46] = 975
				order[47] = 973
				order[48] = 974
				order[49] = 810
				order[50] = 882
				order[51] = 883
				order[52] = 884
				order[53] = 885
				order[54] = 886
				order[55] = 1044
				order[56] = 1045
				order[57] = 1046
				order[58] = 1038
				order[59] = 1039
				order[60] = 315
				order[61] = 1437
				order[62] = 1441
				order[63] = 1453
				order[64] = 1454
				order[65] = 1455
				order[66] = 1456
				order[67] = 1459
				order[68] = 1460
				order[69] = 0
				fix.Group.__init__(self, 711, 311, order)

			class NoUnderlyingSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 458
					order[1] = 459
					order[2] = 0
					fix.Group.__init__(self, 457, 458, order)

			class NoUnderlyingStips(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 888
					order[1] = 889
					order[2] = 0
					fix.Group.__init__(self, 887, 888, order)

			class NoUndlyInstrumentParties(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 1059
					order[1] = 1060
					order[2] = 1061
					order[3] = 1062
					order[4] = 0
					fix.Group.__init__(self, 1058, 1059, order)

				class NoUndlyInstrumentPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1063
						order[1] = 1064
						order[2] = 0
						fix.Group.__init__(self, 1062, 1063, order)

		class NoStipulations(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 233
				order[1] = 234
				order[2] = 0
				fix.Group.__init__(self, 232, 233, order)

		class NoLegs(fix.Group):
			def __init__(self):
				order = fix.IntArray(69)
				order[0] = 600
				order[1] = 601
				order[2] = 602
				order[3] = 603
				order[4] = 1788
				order[5] = 607
				order[6] = 608
				order[7] = 609
				order[8] = 764
				order[9] = 610
				order[10] = 611
				order[11] = 1212
				order[12] = 248
				order[13] = 249
				order[14] = 250
				order[15] = 251
				order[16] = 252
				order[17] = 253
				order[18] = 257
				order[19] = 599
				order[20] = 596
				order[21] = 597
				order[22] = 598
				order[23] = 254
				order[24] = 612
				order[25] = 942
				order[26] = 613
				order[27] = 614
				order[28] = 999
				order[29] = 1224
				order[30] = 1421
				order[31] = 1422
				order[32] = 1001
				order[33] = 1420
				order[34] = 615
				order[35] = 616
				order[36] = 617
				order[37] = 618
				order[38] = 619
				order[39] = 620
				order[40] = 621
				order[41] = 622
				order[42] = 623
				order[43] = 624
				order[44] = 556
				order[45] = 740
				order[46] = 739
				order[47] = 955
				order[48] = 956
				order[49] = 1358
				order[50] = 1017
				order[51] = 1436
				order[52] = 1440
				order[53] = 22041
				order[54] = 22049
				order[55] = 687
				order[56] = 685
				order[57] = 690
				order[58] = 587
				order[59] = 588
				order[60] = 683
				order[61] = 539
				order[62] = 676
				order[63] = 677
				order[64] = 678
				order[65] = 679
				order[66] = 680
				order[67] = 654
				order[68] = 0
				fix.Group.__init__(self, 555, 600, order)

			class NoLegSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 605
					order[1] = 606
					order[2] = 0
					fix.Group.__init__(self, 604, 605, order)

			class NoLegStipulations(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 688
					order[1] = 689
					order[2] = 0
					fix.Group.__init__(self, 683, 688, order)

			class NoNestedPartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 524
					order[1] = 525
					order[2] = 538
					order[3] = 804
					order[4] = 0
					fix.Group.__init__(self, 539, 524, order)

				class NoNestedPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 545
						order[1] = 805
						order[2] = 0
						fix.Group.__init__(self, 804, 545, order)

		class NoQuoteQualifiers(fix.Group):
			def __init__(self):
				order = fix.IntArray(2)
				order[0] = 695
				order[1] = 0
				fix.Group.__init__(self, 735, 695, order)

		class NoPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 448
				order[1] = 447
				order[2] = 452
				order[3] = 2376
				order[4] = 802
				order[5] = 0
				fix.Group.__init__(self, 453, 448, order)

			class NoPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 523
					order[1] = 803
					order[2] = 0
					fix.Group.__init__(self, 802, 523, order)

		class NoRateSources(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1446
				order[1] = 1447
				order[2] = 1448
				order[3] = 0
				fix.Group.__init__(self, 1445, 1446, order)

class Quote(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("S") )

	class NoQuoteQualifiers(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 695
			order[1] = 0
			fix.Group.__init__(self, 735, 695, order)

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(74)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 687
			order[56] = 685
			order[57] = 690
			order[58] = 587
			order[59] = 588
			order[60] = 683
			order[61] = 539
			order[62] = 686
			order[63] = 681
			order[64] = 684
			order[65] = 676
			order[66] = 677
			order[67] = 678
			order[68] = 679
			order[69] = 680
			order[70] = 654
			order[71] = 1067
			order[72] = 1068
			order[73] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

		class NoLegStipulations(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 688
				order[1] = 689
				order[2] = 0
				fix.Group.__init__(self, 683, 688, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

	class NoRateSources(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1446
			order[1] = 1447
			order[2] = 1448
			order[3] = 0
			fix.Group.__init__(self, 1445, 1446, order)

class SettlementInstructions(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("T") )

	class NoSettlInst(fix.Group):
		def __init__(self):
			order = fix.IntArray(26)
			order[0] = 162
			order[1] = 163
			order[2] = 214
			order[3] = 453
			order[4] = 54
			order[5] = 460
			order[6] = 167
			order[7] = 461
			order[8] = 120
			order[9] = 168
			order[10] = 126
			order[11] = 779
			order[12] = 172
			order[13] = 169
			order[14] = 170
			order[15] = 171
			order[16] = 492
			order[17] = 476
			order[18] = 488
			order[19] = 489
			order[20] = 503
			order[21] = 490
			order[22] = 491
			order[23] = 504
			order[24] = 505
			order[25] = 0
			fix.Group.__init__(self, 778, 162, order)

		class NoPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 448
				order[1] = 447
				order[2] = 452
				order[3] = 2376
				order[4] = 802
				order[5] = 0
				fix.Group.__init__(self, 453, 448, order)

			class NoPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 523
					order[1] = 803
					order[2] = 0
					fix.Group.__init__(self, 802, 523, order)

		class NoDlvyInst(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 165
				order[1] = 787
				order[2] = 781
				order[3] = 0
				fix.Group.__init__(self, 85, 165, order)

			class NoSettlPartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 782
					order[1] = 783
					order[2] = 784
					order[3] = 801
					order[4] = 0
					fix.Group.__init__(self, 781, 782, order)

				class NoSettlPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 785
						order[1] = 786
						order[2] = 0
						fix.Group.__init__(self, 801, 785, order)

class MarketDataRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("V") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoMDEntryTypes(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 269
			order[1] = 0
			fix.Group.__init__(self, 267, 269, order)

	class NoRelatedSym(fix.Group):
		def __init__(self):
			order = fix.IntArray(90)
			order[0] = 55
			order[1] = 65
			order[2] = 48
			order[3] = 22
			order[4] = 460
			order[5] = 1227
			order[6] = 1151
			order[7] = 461
			order[8] = 167
			order[9] = 762
			order[10] = 200
			order[11] = 541
			order[12] = 1079
			order[13] = 966
			order[14] = 1049
			order[15] = 965
			order[16] = 224
			order[17] = 225
			order[18] = 239
			order[19] = 226
			order[20] = 227
			order[21] = 228
			order[22] = 255
			order[23] = 543
			order[24] = 470
			order[25] = 471
			order[26] = 472
			order[27] = 240
			order[28] = 202
			order[29] = 947
			order[30] = 967
			order[31] = 968
			order[32] = 206
			order[33] = 231
			order[34] = 969
			order[35] = 1146
			order[36] = 996
			order[37] = 1147
			order[38] = 1191
			order[39] = 1192
			order[40] = 1193
			order[41] = 1194
			order[42] = 1195
			order[43] = 1196
			order[44] = 1197
			order[45] = 1198
			order[46] = 1199
			order[47] = 1200
			order[48] = 201
			order[49] = 1244
			order[50] = 1242
			order[51] = 997
			order[52] = 223
			order[53] = 207
			order[54] = 970
			order[55] = 971
			order[56] = 106
			order[57] = 348
			order[58] = 349
			order[59] = 107
			order[60] = 350
			order[61] = 351
			order[62] = 691
			order[63] = 667
			order[64] = 875
			order[65] = 876
			order[66] = 873
			order[67] = 874
			order[68] = 1435
			order[69] = 1439
			order[70] = 1449
			order[71] = 1450
			order[72] = 1451
			order[73] = 1452
			order[74] = 1457
			order[75] = 1458
			order[76] = 1478
			order[77] = 1479
			order[78] = 1480
			order[79] = 1481
			order[80] = 1482
			order[81] = 711
			order[82] = 555
			order[83] = 15
			order[84] = 537
			order[85] = 63
			order[86] = 64
			order[87] = 271
			order[88] = 1500
			order[89] = 0
			fix.Group.__init__(self, 146, 55, order)

		class NoSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 455
				order[1] = 456
				order[2] = 0
				fix.Group.__init__(self, 454, 455, order)

		class NoEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 865
				order[1] = 866
				order[2] = 1145
				order[3] = 867
				order[4] = 868
				order[5] = 0
				fix.Group.__init__(self, 864, 865, order)

		class NoInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1019
				order[1] = 1050
				order[2] = 1051
				order[3] = 1052
				order[4] = 0
				fix.Group.__init__(self, 1018, 1019, order)

			class NoInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1053
					order[1] = 1054
					order[2] = 0
					fix.Group.__init__(self, 1052, 1053, order)

		class NoComplexEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(9)
				order[0] = 1484
				order[1] = 1485
				order[2] = 1486
				order[3] = 1487
				order[4] = 1488
				order[5] = 1489
				order[6] = 1490
				order[7] = 1491
				order[8] = 0
				fix.Group.__init__(self, 1483, 1484, order)

			class NoComplexEventDates(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1492
					order[1] = 1493
					order[2] = 1494
					order[3] = 0
					fix.Group.__init__(self, 1491, 1492, order)

				class NoComplexEventTimes(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1495
						order[1] = 1496
						order[2] = 0
						fix.Group.__init__(self, 1494, 1495, order)

		class NoUnderlyings(fix.Group):
			def __init__(self):
				order = fix.IntArray(70)
				order[0] = 311
				order[1] = 312
				order[2] = 309
				order[3] = 305
				order[4] = 462
				order[5] = 463
				order[6] = 310
				order[7] = 763
				order[8] = 313
				order[9] = 542
				order[10] = 1213
				order[11] = 241
				order[12] = 242
				order[13] = 243
				order[14] = 244
				order[15] = 245
				order[16] = 246
				order[17] = 256
				order[18] = 595
				order[19] = 592
				order[20] = 593
				order[21] = 594
				order[22] = 247
				order[23] = 316
				order[24] = 941
				order[25] = 317
				order[26] = 436
				order[27] = 998
				order[28] = 1423
				order[29] = 1424
				order[30] = 1425
				order[31] = 1000
				order[32] = 1419
				order[33] = 435
				order[34] = 308
				order[35] = 306
				order[36] = 362
				order[37] = 363
				order[38] = 307
				order[39] = 364
				order[40] = 365
				order[41] = 877
				order[42] = 878
				order[43] = 972
				order[44] = 318
				order[45] = 879
				order[46] = 975
				order[47] = 973
				order[48] = 974
				order[49] = 810
				order[50] = 882
				order[51] = 883
				order[52] = 884
				order[53] = 885
				order[54] = 886
				order[55] = 1044
				order[56] = 1045
				order[57] = 1046
				order[58] = 1038
				order[59] = 1039
				order[60] = 315
				order[61] = 1437
				order[62] = 1441
				order[63] = 1453
				order[64] = 1454
				order[65] = 1455
				order[66] = 1456
				order[67] = 1459
				order[68] = 1460
				order[69] = 0
				fix.Group.__init__(self, 711, 311, order)

			class NoUnderlyingSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 458
					order[1] = 459
					order[2] = 0
					fix.Group.__init__(self, 457, 458, order)

			class NoUnderlyingStips(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 888
					order[1] = 889
					order[2] = 0
					fix.Group.__init__(self, 887, 888, order)

			class NoUndlyInstrumentParties(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 1059
					order[1] = 1060
					order[2] = 1061
					order[3] = 1062
					order[4] = 0
					fix.Group.__init__(self, 1058, 1059, order)

				class NoUndlyInstrumentPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1063
						order[1] = 1064
						order[2] = 0
						fix.Group.__init__(self, 1062, 1063, order)

		class NoLegs(fix.Group):
			def __init__(self):
				order = fix.IntArray(56)
				order[0] = 600
				order[1] = 601
				order[2] = 602
				order[3] = 603
				order[4] = 1788
				order[5] = 607
				order[6] = 608
				order[7] = 609
				order[8] = 764
				order[9] = 610
				order[10] = 611
				order[11] = 1212
				order[12] = 248
				order[13] = 249
				order[14] = 250
				order[15] = 251
				order[16] = 252
				order[17] = 253
				order[18] = 257
				order[19] = 599
				order[20] = 596
				order[21] = 597
				order[22] = 598
				order[23] = 254
				order[24] = 612
				order[25] = 942
				order[26] = 613
				order[27] = 614
				order[28] = 999
				order[29] = 1224
				order[30] = 1421
				order[31] = 1422
				order[32] = 1001
				order[33] = 1420
				order[34] = 615
				order[35] = 616
				order[36] = 617
				order[37] = 618
				order[38] = 619
				order[39] = 620
				order[40] = 621
				order[41] = 622
				order[42] = 623
				order[43] = 624
				order[44] = 556
				order[45] = 740
				order[46] = 739
				order[47] = 955
				order[48] = 956
				order[49] = 1358
				order[50] = 1017
				order[51] = 1436
				order[52] = 1440
				order[53] = 22041
				order[54] = 22049
				order[55] = 0
				fix.Group.__init__(self, 555, 600, order)

			class NoLegSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 605
					order[1] = 606
					order[2] = 0
					fix.Group.__init__(self, 604, 605, order)

	class NoTradingSessions(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 336
			order[1] = 625
			order[2] = 0
			fix.Group.__init__(self, 386, 336, order)

class MarketDataSnapshotFullRefresh(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("W") )

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoMDEntries(fix.Group):
		def __init__(self):
			order = fix.IntArray(79)
			order[0] = 269
			order[1] = 278
			order[2] = 270
			order[3] = 423
			order[4] = 235
			order[5] = 236
			order[6] = 701
			order[7] = 696
			order[8] = 697
			order[9] = 698
			order[10] = 218
			order[11] = 22048
			order[12] = 220
			order[13] = 221
			order[14] = 222
			order[15] = 662
			order[16] = 663
			order[17] = 699
			order[18] = 761
			order[19] = 40
			order[20] = 15
			order[21] = 1742
			order[22] = 1741
			order[23] = 271
			order[24] = 746
			order[25] = 1177
			order[26] = 1093
			order[27] = 272
			order[28] = 273
			order[29] = 274
			order[30] = 275
			order[31] = 336
			order[32] = 625
			order[33] = 326
			order[34] = 327
			order[35] = 276
			order[36] = 277
			order[37] = 282
			order[38] = 283
			order[39] = 284
			order[40] = 286
			order[41] = 59
			order[42] = 432
			order[43] = 126
			order[44] = 110
			order[45] = 18
			order[46] = 287
			order[47] = 37
			order[48] = 198
			order[49] = 299
			order[50] = 288
			order[51] = 289
			order[52] = 346
			order[53] = 290
			order[54] = 546
			order[55] = 811
			order[56] = 58
			order[57] = 354
			order[58] = 355
			order[59] = 1023
			order[60] = 528
			order[61] = 1024
			order[62] = 332
			order[63] = 333
			order[64] = 1020
			order[65] = 63
			order[66] = 64
			order[67] = 1070
			order[68] = 83
			order[69] = 1048
			order[70] = 1026
			order[71] = 1027
			order[72] = 453
			order[73] = 120
			order[74] = 1445
			order[75] = 828
			order[76] = 1025
			order[77] = 31
			order[78] = 0
			fix.Group.__init__(self, 268, 269, order)

		class NoOfSecSizes(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1178
				order[1] = 1179
				order[2] = 0
				fix.Group.__init__(self, 1177, 1178, order)

		class NoPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 448
				order[1] = 447
				order[2] = 452
				order[3] = 2376
				order[4] = 802
				order[5] = 0
				fix.Group.__init__(self, 453, 448, order)

			class NoPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 523
					order[1] = 803
					order[2] = 0
					fix.Group.__init__(self, 802, 523, order)

		class NoRateSources(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1446
				order[1] = 1447
				order[2] = 1448
				order[3] = 0
				fix.Group.__init__(self, 1445, 1446, order)

	class NoRoutingIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 216
			order[1] = 217
			order[2] = 0
			fix.Group.__init__(self, 215, 216, order)

class MarketDataIncrementalRefresh(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("X") )

	class NoMDEntries(fix.Group):
		def __init__(self):
			order = fix.IntArray(175)
			order[0] = 279
			order[1] = 285
			order[2] = 1173
			order[3] = 264
			order[4] = 269
			order[5] = 278
			order[6] = 280
			order[7] = 55
			order[8] = 65
			order[9] = 48
			order[10] = 22
			order[11] = 460
			order[12] = 1227
			order[13] = 1151
			order[14] = 461
			order[15] = 167
			order[16] = 762
			order[17] = 200
			order[18] = 541
			order[19] = 1079
			order[20] = 966
			order[21] = 1049
			order[22] = 965
			order[23] = 224
			order[24] = 225
			order[25] = 239
			order[26] = 226
			order[27] = 227
			order[28] = 228
			order[29] = 255
			order[30] = 543
			order[31] = 470
			order[32] = 471
			order[33] = 472
			order[34] = 240
			order[35] = 202
			order[36] = 947
			order[37] = 967
			order[38] = 968
			order[39] = 206
			order[40] = 231
			order[41] = 969
			order[42] = 1146
			order[43] = 996
			order[44] = 1147
			order[45] = 1191
			order[46] = 1192
			order[47] = 1193
			order[48] = 1194
			order[49] = 1195
			order[50] = 1196
			order[51] = 1197
			order[52] = 1198
			order[53] = 1199
			order[54] = 1200
			order[55] = 201
			order[56] = 1244
			order[57] = 1242
			order[58] = 997
			order[59] = 223
			order[60] = 207
			order[61] = 970
			order[62] = 971
			order[63] = 106
			order[64] = 348
			order[65] = 349
			order[66] = 107
			order[67] = 350
			order[68] = 351
			order[69] = 691
			order[70] = 667
			order[71] = 875
			order[72] = 876
			order[73] = 873
			order[74] = 874
			order[75] = 1435
			order[76] = 1439
			order[77] = 1449
			order[78] = 1450
			order[79] = 1451
			order[80] = 1452
			order[81] = 1457
			order[82] = 1458
			order[83] = 1478
			order[84] = 1479
			order[85] = 1480
			order[86] = 1481
			order[87] = 1482
			order[88] = 711
			order[89] = 555
			order[90] = 291
			order[91] = 292
			order[92] = 270
			order[93] = 423
			order[94] = 235
			order[95] = 236
			order[96] = 701
			order[97] = 696
			order[98] = 697
			order[99] = 698
			order[100] = 218
			order[101] = 22048
			order[102] = 220
			order[103] = 221
			order[104] = 222
			order[105] = 662
			order[106] = 663
			order[107] = 699
			order[108] = 761
			order[109] = 40
			order[110] = 15
			order[111] = 271
			order[112] = 1177
			order[113] = 1093
			order[114] = 272
			order[115] = 273
			order[116] = 274
			order[117] = 275
			order[118] = 336
			order[119] = 625
			order[120] = 326
			order[121] = 327
			order[122] = 276
			order[123] = 277
			order[124] = 828
			order[125] = 574
			order[126] = 282
			order[127] = 283
			order[128] = 284
			order[129] = 286
			order[130] = 59
			order[131] = 432
			order[132] = 126
			order[133] = 110
			order[134] = 18
			order[135] = 287
			order[136] = 37
			order[137] = 198
			order[138] = 299
			order[139] = 1003
			order[140] = 288
			order[141] = 289
			order[142] = 346
			order[143] = 290
			order[144] = 546
			order[145] = 811
			order[146] = 451
			order[147] = 58
			order[148] = 354
			order[149] = 355
			order[150] = 1023
			order[151] = 528
			order[152] = 1024
			order[153] = 332
			order[154] = 333
			order[155] = 1020
			order[156] = 63
			order[157] = 64
			order[158] = 483
			order[159] = 60
			order[160] = 1070
			order[161] = 22050
			order[162] = 22051
			order[163] = 83
			order[164] = 1048
			order[165] = 1026
			order[166] = 1027
			order[167] = 1175
			order[168] = 453
			order[169] = 120
			order[170] = 1445
			order[171] = 1025
			order[172] = 31
			order[173] = 1500
			order[174] = 0
			fix.Group.__init__(self, 268, 279, order)

		class NoSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 455
				order[1] = 456
				order[2] = 0
				fix.Group.__init__(self, 454, 455, order)

		class NoEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 865
				order[1] = 866
				order[2] = 1145
				order[3] = 867
				order[4] = 868
				order[5] = 0
				fix.Group.__init__(self, 864, 865, order)

		class NoInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1019
				order[1] = 1050
				order[2] = 1051
				order[3] = 1052
				order[4] = 0
				fix.Group.__init__(self, 1018, 1019, order)

			class NoInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1053
					order[1] = 1054
					order[2] = 0
					fix.Group.__init__(self, 1052, 1053, order)

		class NoComplexEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(9)
				order[0] = 1484
				order[1] = 1485
				order[2] = 1486
				order[3] = 1487
				order[4] = 1488
				order[5] = 1489
				order[6] = 1490
				order[7] = 1491
				order[8] = 0
				fix.Group.__init__(self, 1483, 1484, order)

			class NoComplexEventDates(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1492
					order[1] = 1493
					order[2] = 1494
					order[3] = 0
					fix.Group.__init__(self, 1491, 1492, order)

				class NoComplexEventTimes(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1495
						order[1] = 1496
						order[2] = 0
						fix.Group.__init__(self, 1494, 1495, order)

		class NoUnderlyings(fix.Group):
			def __init__(self):
				order = fix.IntArray(70)
				order[0] = 311
				order[1] = 312
				order[2] = 309
				order[3] = 305
				order[4] = 462
				order[5] = 463
				order[6] = 310
				order[7] = 763
				order[8] = 313
				order[9] = 542
				order[10] = 1213
				order[11] = 241
				order[12] = 242
				order[13] = 243
				order[14] = 244
				order[15] = 245
				order[16] = 246
				order[17] = 256
				order[18] = 595
				order[19] = 592
				order[20] = 593
				order[21] = 594
				order[22] = 247
				order[23] = 316
				order[24] = 941
				order[25] = 317
				order[26] = 436
				order[27] = 998
				order[28] = 1423
				order[29] = 1424
				order[30] = 1425
				order[31] = 1000
				order[32] = 1419
				order[33] = 435
				order[34] = 308
				order[35] = 306
				order[36] = 362
				order[37] = 363
				order[38] = 307
				order[39] = 364
				order[40] = 365
				order[41] = 877
				order[42] = 878
				order[43] = 972
				order[44] = 318
				order[45] = 879
				order[46] = 975
				order[47] = 973
				order[48] = 974
				order[49] = 810
				order[50] = 882
				order[51] = 883
				order[52] = 884
				order[53] = 885
				order[54] = 886
				order[55] = 1044
				order[56] = 1045
				order[57] = 1046
				order[58] = 1038
				order[59] = 1039
				order[60] = 315
				order[61] = 1437
				order[62] = 1441
				order[63] = 1453
				order[64] = 1454
				order[65] = 1455
				order[66] = 1456
				order[67] = 1459
				order[68] = 1460
				order[69] = 0
				fix.Group.__init__(self, 711, 311, order)

			class NoUnderlyingSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 458
					order[1] = 459
					order[2] = 0
					fix.Group.__init__(self, 457, 458, order)

			class NoUnderlyingStips(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 888
					order[1] = 889
					order[2] = 0
					fix.Group.__init__(self, 887, 888, order)

			class NoUndlyInstrumentParties(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 1059
					order[1] = 1060
					order[2] = 1061
					order[3] = 1062
					order[4] = 0
					fix.Group.__init__(self, 1058, 1059, order)

				class NoUndlyInstrumentPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1063
						order[1] = 1064
						order[2] = 0
						fix.Group.__init__(self, 1062, 1063, order)

		class NoLegs(fix.Group):
			def __init__(self):
				order = fix.IntArray(56)
				order[0] = 600
				order[1] = 601
				order[2] = 602
				order[3] = 603
				order[4] = 1788
				order[5] = 607
				order[6] = 608
				order[7] = 609
				order[8] = 764
				order[9] = 610
				order[10] = 611
				order[11] = 1212
				order[12] = 248
				order[13] = 249
				order[14] = 250
				order[15] = 251
				order[16] = 252
				order[17] = 253
				order[18] = 257
				order[19] = 599
				order[20] = 596
				order[21] = 597
				order[22] = 598
				order[23] = 254
				order[24] = 612
				order[25] = 942
				order[26] = 613
				order[27] = 614
				order[28] = 999
				order[29] = 1224
				order[30] = 1421
				order[31] = 1422
				order[32] = 1001
				order[33] = 1420
				order[34] = 615
				order[35] = 616
				order[36] = 617
				order[37] = 618
				order[38] = 619
				order[39] = 620
				order[40] = 621
				order[41] = 622
				order[42] = 623
				order[43] = 624
				order[44] = 556
				order[45] = 740
				order[46] = 739
				order[47] = 955
				order[48] = 956
				order[49] = 1358
				order[50] = 1017
				order[51] = 1436
				order[52] = 1440
				order[53] = 22041
				order[54] = 22049
				order[55] = 0
				fix.Group.__init__(self, 555, 600, order)

			class NoLegSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 605
					order[1] = 606
					order[2] = 0
					fix.Group.__init__(self, 604, 605, order)

		class NoOfSecSizes(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1178
				order[1] = 1179
				order[2] = 0
				fix.Group.__init__(self, 1177, 1178, order)

		class NoStatsIndicators(fix.Group):
			def __init__(self):
				order = fix.IntArray(2)
				order[0] = 1176
				order[1] = 0
				fix.Group.__init__(self, 1175, 1176, order)

		class NoPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 448
				order[1] = 447
				order[2] = 452
				order[3] = 2376
				order[4] = 802
				order[5] = 0
				fix.Group.__init__(self, 453, 448, order)

			class NoPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 523
					order[1] = 803
					order[2] = 0
					fix.Group.__init__(self, 802, 523, order)

		class NoRateSources(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1446
				order[1] = 1447
				order[2] = 1448
				order[3] = 0
				fix.Group.__init__(self, 1445, 1446, order)

	class NoRoutingIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 216
			order[1] = 217
			order[2] = 0
			fix.Group.__init__(self, 215, 216, order)

class MarketDataRequestReject(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("Y") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoAltMDSource(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 817
			order[1] = 0
			fix.Group.__init__(self, 816, 817, order)

class QuoteCancel(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("Z") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoQuoteEntries(fix.Group):
		def __init__(self):
			order = fix.IntArray(93)
			order[0] = 55
			order[1] = 65
			order[2] = 48
			order[3] = 22
			order[4] = 460
			order[5] = 1227
			order[6] = 1151
			order[7] = 461
			order[8] = 167
			order[9] = 762
			order[10] = 200
			order[11] = 541
			order[12] = 1079
			order[13] = 966
			order[14] = 1049
			order[15] = 965
			order[16] = 224
			order[17] = 225
			order[18] = 239
			order[19] = 226
			order[20] = 227
			order[21] = 228
			order[22] = 255
			order[23] = 543
			order[24] = 470
			order[25] = 471
			order[26] = 472
			order[27] = 240
			order[28] = 202
			order[29] = 947
			order[30] = 967
			order[31] = 968
			order[32] = 206
			order[33] = 231
			order[34] = 969
			order[35] = 1146
			order[36] = 996
			order[37] = 1147
			order[38] = 1191
			order[39] = 1192
			order[40] = 1193
			order[41] = 1194
			order[42] = 1195
			order[43] = 1196
			order[44] = 1197
			order[45] = 1198
			order[46] = 1199
			order[47] = 1200
			order[48] = 201
			order[49] = 1244
			order[50] = 1242
			order[51] = 997
			order[52] = 223
			order[53] = 207
			order[54] = 970
			order[55] = 971
			order[56] = 106
			order[57] = 348
			order[58] = 349
			order[59] = 107
			order[60] = 350
			order[61] = 351
			order[62] = 691
			order[63] = 667
			order[64] = 875
			order[65] = 876
			order[66] = 873
			order[67] = 874
			order[68] = 1435
			order[69] = 1439
			order[70] = 1449
			order[71] = 1450
			order[72] = 1451
			order[73] = 1452
			order[74] = 1457
			order[75] = 1458
			order[76] = 1478
			order[77] = 1479
			order[78] = 1480
			order[79] = 1481
			order[80] = 1482
			order[81] = 913
			order[82] = 914
			order[83] = 915
			order[84] = 918
			order[85] = 788
			order[86] = 916
			order[87] = 917
			order[88] = 919
			order[89] = 898
			order[90] = 711
			order[91] = 555
			order[92] = 0
			fix.Group.__init__(self, 295, 55, order)

		class NoSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 455
				order[1] = 456
				order[2] = 0
				fix.Group.__init__(self, 454, 455, order)

		class NoEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 865
				order[1] = 866
				order[2] = 1145
				order[3] = 867
				order[4] = 868
				order[5] = 0
				fix.Group.__init__(self, 864, 865, order)

		class NoInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1019
				order[1] = 1050
				order[2] = 1051
				order[3] = 1052
				order[4] = 0
				fix.Group.__init__(self, 1018, 1019, order)

			class NoInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1053
					order[1] = 1054
					order[2] = 0
					fix.Group.__init__(self, 1052, 1053, order)

		class NoComplexEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(9)
				order[0] = 1484
				order[1] = 1485
				order[2] = 1486
				order[3] = 1487
				order[4] = 1488
				order[5] = 1489
				order[6] = 1490
				order[7] = 1491
				order[8] = 0
				fix.Group.__init__(self, 1483, 1484, order)

			class NoComplexEventDates(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1492
					order[1] = 1493
					order[2] = 1494
					order[3] = 0
					fix.Group.__init__(self, 1491, 1492, order)

				class NoComplexEventTimes(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1495
						order[1] = 1496
						order[2] = 0
						fix.Group.__init__(self, 1494, 1495, order)

		class NoUnderlyings(fix.Group):
			def __init__(self):
				order = fix.IntArray(70)
				order[0] = 311
				order[1] = 312
				order[2] = 309
				order[3] = 305
				order[4] = 462
				order[5] = 463
				order[6] = 310
				order[7] = 763
				order[8] = 313
				order[9] = 542
				order[10] = 1213
				order[11] = 241
				order[12] = 242
				order[13] = 243
				order[14] = 244
				order[15] = 245
				order[16] = 246
				order[17] = 256
				order[18] = 595
				order[19] = 592
				order[20] = 593
				order[21] = 594
				order[22] = 247
				order[23] = 316
				order[24] = 941
				order[25] = 317
				order[26] = 436
				order[27] = 998
				order[28] = 1423
				order[29] = 1424
				order[30] = 1425
				order[31] = 1000
				order[32] = 1419
				order[33] = 435
				order[34] = 308
				order[35] = 306
				order[36] = 362
				order[37] = 363
				order[38] = 307
				order[39] = 364
				order[40] = 365
				order[41] = 877
				order[42] = 878
				order[43] = 972
				order[44] = 318
				order[45] = 879
				order[46] = 975
				order[47] = 973
				order[48] = 974
				order[49] = 810
				order[50] = 882
				order[51] = 883
				order[52] = 884
				order[53] = 885
				order[54] = 886
				order[55] = 1044
				order[56] = 1045
				order[57] = 1046
				order[58] = 1038
				order[59] = 1039
				order[60] = 315
				order[61] = 1437
				order[62] = 1441
				order[63] = 1453
				order[64] = 1454
				order[65] = 1455
				order[66] = 1456
				order[67] = 1459
				order[68] = 1460
				order[69] = 0
				fix.Group.__init__(self, 711, 311, order)

			class NoUnderlyingSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 458
					order[1] = 459
					order[2] = 0
					fix.Group.__init__(self, 457, 458, order)

			class NoUnderlyingStips(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 888
					order[1] = 889
					order[2] = 0
					fix.Group.__init__(self, 887, 888, order)

			class NoUndlyInstrumentParties(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 1059
					order[1] = 1060
					order[2] = 1061
					order[3] = 1062
					order[4] = 0
					fix.Group.__init__(self, 1058, 1059, order)

				class NoUndlyInstrumentPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1063
						order[1] = 1064
						order[2] = 0
						fix.Group.__init__(self, 1062, 1063, order)

		class NoLegs(fix.Group):
			def __init__(self):
				order = fix.IntArray(56)
				order[0] = 600
				order[1] = 601
				order[2] = 602
				order[3] = 603
				order[4] = 1788
				order[5] = 607
				order[6] = 608
				order[7] = 609
				order[8] = 764
				order[9] = 610
				order[10] = 611
				order[11] = 1212
				order[12] = 248
				order[13] = 249
				order[14] = 250
				order[15] = 251
				order[16] = 252
				order[17] = 253
				order[18] = 257
				order[19] = 599
				order[20] = 596
				order[21] = 597
				order[22] = 598
				order[23] = 254
				order[24] = 612
				order[25] = 942
				order[26] = 613
				order[27] = 614
				order[28] = 999
				order[29] = 1224
				order[30] = 1421
				order[31] = 1422
				order[32] = 1001
				order[33] = 1420
				order[34] = 615
				order[35] = 616
				order[36] = 617
				order[37] = 618
				order[38] = 619
				order[39] = 620
				order[40] = 621
				order[41] = 622
				order[42] = 623
				order[43] = 624
				order[44] = 556
				order[45] = 740
				order[46] = 739
				order[47] = 955
				order[48] = 956
				order[49] = 1358
				order[50] = 1017
				order[51] = 1436
				order[52] = 1440
				order[53] = 22041
				order[54] = 22049
				order[55] = 0
				fix.Group.__init__(self, 555, 600, order)

			class NoLegSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 605
					order[1] = 606
					order[2] = 0
					fix.Group.__init__(self, 604, 605, order)

	class NoTargetPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1462
			order[1] = 1463
			order[2] = 1464
			order[3] = 0
			fix.Group.__init__(self, 1461, 1462, order)

class QuoteStatusRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("a") )

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoTargetPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1462
			order[1] = 1463
			order[2] = 1464
			order[3] = 0
			fix.Group.__init__(self, 1461, 1462, order)

class MassQuoteAcknowledgement(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("b") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoQuoteSets(fix.Group):
		def __init__(self):
			order = fix.IntArray(78)
			order[0] = 302
			order[1] = 311
			order[2] = 312
			order[3] = 309
			order[4] = 305
			order[5] = 462
			order[6] = 463
			order[7] = 310
			order[8] = 763
			order[9] = 313
			order[10] = 542
			order[11] = 1213
			order[12] = 241
			order[13] = 242
			order[14] = 243
			order[15] = 244
			order[16] = 245
			order[17] = 246
			order[18] = 256
			order[19] = 595
			order[20] = 592
			order[21] = 593
			order[22] = 594
			order[23] = 247
			order[24] = 316
			order[25] = 941
			order[26] = 317
			order[27] = 436
			order[28] = 998
			order[29] = 1423
			order[30] = 1424
			order[31] = 1425
			order[32] = 1000
			order[33] = 1419
			order[34] = 435
			order[35] = 308
			order[36] = 306
			order[37] = 362
			order[38] = 363
			order[39] = 307
			order[40] = 364
			order[41] = 365
			order[42] = 877
			order[43] = 878
			order[44] = 972
			order[45] = 318
			order[46] = 879
			order[47] = 975
			order[48] = 973
			order[49] = 974
			order[50] = 810
			order[51] = 882
			order[52] = 883
			order[53] = 884
			order[54] = 885
			order[55] = 886
			order[56] = 1044
			order[57] = 1045
			order[58] = 1046
			order[59] = 1038
			order[60] = 1039
			order[61] = 315
			order[62] = 1437
			order[63] = 1441
			order[64] = 1453
			order[65] = 1454
			order[66] = 1455
			order[67] = 1456
			order[68] = 1459
			order[69] = 1460
			order[70] = 304
			order[71] = 1168
			order[72] = 1169
			order[73] = 1170
			order[74] = 893
			order[75] = 295
			order[76] = 367
			order[77] = 0
			fix.Group.__init__(self, 296, 302, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

		class NoQuoteEntries(fix.Group):
			def __init__(self):
				order = fix.IntArray(112)
				order[0] = 299
				order[1] = 55
				order[2] = 65
				order[3] = 48
				order[4] = 22
				order[5] = 460
				order[6] = 1227
				order[7] = 1151
				order[8] = 461
				order[9] = 167
				order[10] = 762
				order[11] = 200
				order[12] = 541
				order[13] = 1079
				order[14] = 966
				order[15] = 1049
				order[16] = 965
				order[17] = 224
				order[18] = 225
				order[19] = 239
				order[20] = 226
				order[21] = 227
				order[22] = 228
				order[23] = 255
				order[24] = 543
				order[25] = 470
				order[26] = 471
				order[27] = 472
				order[28] = 240
				order[29] = 202
				order[30] = 947
				order[31] = 967
				order[32] = 968
				order[33] = 206
				order[34] = 231
				order[35] = 969
				order[36] = 1146
				order[37] = 996
				order[38] = 1147
				order[39] = 1191
				order[40] = 1192
				order[41] = 1193
				order[42] = 1194
				order[43] = 1195
				order[44] = 1196
				order[45] = 1197
				order[46] = 1198
				order[47] = 1199
				order[48] = 1200
				order[49] = 201
				order[50] = 1244
				order[51] = 1242
				order[52] = 997
				order[53] = 223
				order[54] = 207
				order[55] = 970
				order[56] = 971
				order[57] = 106
				order[58] = 348
				order[59] = 349
				order[60] = 107
				order[61] = 350
				order[62] = 351
				order[63] = 691
				order[64] = 667
				order[65] = 875
				order[66] = 876
				order[67] = 873
				order[68] = 874
				order[69] = 1435
				order[70] = 1439
				order[71] = 1449
				order[72] = 1450
				order[73] = 1451
				order[74] = 1452
				order[75] = 1457
				order[76] = 1458
				order[77] = 1478
				order[78] = 1479
				order[79] = 1480
				order[80] = 1481
				order[81] = 1482
				order[82] = 555
				order[83] = 132
				order[84] = 133
				order[85] = 134
				order[86] = 135
				order[87] = 62
				order[88] = 188
				order[89] = 190
				order[90] = 189
				order[91] = 191
				order[92] = 631
				order[93] = 632
				order[94] = 633
				order[95] = 634
				order[96] = 60
				order[97] = 336
				order[98] = 625
				order[99] = 64
				order[100] = 40
				order[101] = 193
				order[102] = 192
				order[103] = 642
				order[104] = 643
				order[105] = 15
				order[106] = 1167
				order[107] = 368
				order[108] = 775
				order[109] = 528
				order[110] = 529
				order[111] = 0
				fix.Group.__init__(self, 295, 299, order)

			class NoSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 455
					order[1] = 456
					order[2] = 0
					fix.Group.__init__(self, 454, 455, order)

			class NoEvents(fix.Group):
				def __init__(self):
					order = fix.IntArray(6)
					order[0] = 865
					order[1] = 866
					order[2] = 1145
					order[3] = 867
					order[4] = 868
					order[5] = 0
					fix.Group.__init__(self, 864, 865, order)

			class NoInstrumentParties(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 1019
					order[1] = 1050
					order[2] = 1051
					order[3] = 1052
					order[4] = 0
					fix.Group.__init__(self, 1018, 1019, order)

				class NoInstrumentPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1053
						order[1] = 1054
						order[2] = 0
						fix.Group.__init__(self, 1052, 1053, order)

			class NoComplexEvents(fix.Group):
				def __init__(self):
					order = fix.IntArray(9)
					order[0] = 1484
					order[1] = 1485
					order[2] = 1486
					order[3] = 1487
					order[4] = 1488
					order[5] = 1489
					order[6] = 1490
					order[7] = 1491
					order[8] = 0
					fix.Group.__init__(self, 1483, 1484, order)

				class NoComplexEventDates(fix.Group):
					def __init__(self):
						order = fix.IntArray(4)
						order[0] = 1492
						order[1] = 1493
						order[2] = 1494
						order[3] = 0
						fix.Group.__init__(self, 1491, 1492, order)

					class NoComplexEventTimes(fix.Group):
						def __init__(self):
							order = fix.IntArray(3)
							order[0] = 1495
							order[1] = 1496
							order[2] = 0
							fix.Group.__init__(self, 1494, 1495, order)

			class NoLegs(fix.Group):
				def __init__(self):
					order = fix.IntArray(56)
					order[0] = 600
					order[1] = 601
					order[2] = 602
					order[3] = 603
					order[4] = 1788
					order[5] = 607
					order[6] = 608
					order[7] = 609
					order[8] = 764
					order[9] = 610
					order[10] = 611
					order[11] = 1212
					order[12] = 248
					order[13] = 249
					order[14] = 250
					order[15] = 251
					order[16] = 252
					order[17] = 253
					order[18] = 257
					order[19] = 599
					order[20] = 596
					order[21] = 597
					order[22] = 598
					order[23] = 254
					order[24] = 612
					order[25] = 942
					order[26] = 613
					order[27] = 614
					order[28] = 999
					order[29] = 1224
					order[30] = 1421
					order[31] = 1422
					order[32] = 1001
					order[33] = 1420
					order[34] = 615
					order[35] = 616
					order[36] = 617
					order[37] = 618
					order[38] = 619
					order[39] = 620
					order[40] = 621
					order[41] = 622
					order[42] = 623
					order[43] = 624
					order[44] = 556
					order[45] = 740
					order[46] = 739
					order[47] = 955
					order[48] = 956
					order[49] = 1358
					order[50] = 1017
					order[51] = 1436
					order[52] = 1440
					order[53] = 22041
					order[54] = 22049
					order[55] = 0
					fix.Group.__init__(self, 555, 600, order)

				class NoLegSecurityAltID(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 605
						order[1] = 606
						order[2] = 0
						fix.Group.__init__(self, 604, 605, order)

	class NoTargetPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1462
			order[1] = 1463
			order[2] = 1464
			order[3] = 0
			fix.Group.__init__(self, 1461, 1462, order)

class SecurityDefinitionRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("c") )

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoInstrAttrib(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 871
			order[1] = 872
			order[2] = 0
			fix.Group.__init__(self, 870, 871, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

class SecurityDefinition(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("d") )

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoInstrAttrib(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 871
			order[1] = 872
			order[2] = 0
			fix.Group.__init__(self, 870, 871, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoMarketSegments(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1301
			order[1] = 1300
			order[2] = 1201
			order[3] = 0
			fix.Group.__init__(self, 1310, 1301, order)

		class NoTickRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1206
				order[1] = 1207
				order[2] = 1208
				order[3] = 1209
				order[4] = 0
				fix.Group.__init__(self, 1205, 1206, order)

		class NoLotTypeRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1093
				order[1] = 1231
				order[2] = 0
				fix.Group.__init__(self, 1234, 1093, order)

		class NoTradingSessionRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 336
				order[1] = 625
				order[2] = 0
				fix.Group.__init__(self, 1309, 336, order)

			class NoOrdTypeRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 40
					order[1] = 0
					fix.Group.__init__(self, 1237, 40, order)

			class NoTimeInForceRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 59
					order[1] = 0
					fix.Group.__init__(self, 1239, 59, order)

			class NoExecInstRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 1308
					order[1] = 0
					fix.Group.__init__(self, 1232, 1308, order)

			class NoMatchRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1142
					order[1] = 574
					order[2] = 0
					fix.Group.__init__(self, 1235, 1142, order)

			class NoMDFeedTypes(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1022
					order[1] = 264
					order[2] = 1021
					order[3] = 0
					fix.Group.__init__(self, 1141, 1022, order)

		class NoNestedInstrAttrib(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1210
				order[1] = 1211
				order[2] = 0
				fix.Group.__init__(self, 1312, 1210, order)

		class NoStrikeRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(7)
				order[0] = 1223
				order[1] = 1202
				order[2] = 1203
				order[3] = 1204
				order[4] = 1304
				order[5] = 1236
				order[6] = 0
				fix.Group.__init__(self, 1201, 1223, order)

			class NoMaturityRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(7)
					order[0] = 1222
					order[1] = 1303
					order[2] = 1302
					order[3] = 1241
					order[4] = 1226
					order[5] = 1229
					order[6] = 0
					fix.Group.__init__(self, 1236, 1222, order)

class SecurityStatusRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("e") )

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoInstrAttrib(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 871
			order[1] = 872
			order[2] = 0
			fix.Group.__init__(self, 870, 871, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

class SecurityStatus(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("f") )

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoInstrAttrib(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 871
			order[1] = 872
			order[2] = 0
			fix.Group.__init__(self, 870, 871, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

class TradingSessionStatusRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("g") )

class TradingSessionStatus(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("h") )

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

class MassQuote(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("i") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoQuoteSets(fix.Group):
		def __init__(self):
			order = fix.IntArray(75)
			order[0] = 302
			order[1] = 311
			order[2] = 312
			order[3] = 309
			order[4] = 305
			order[5] = 462
			order[6] = 463
			order[7] = 310
			order[8] = 763
			order[9] = 313
			order[10] = 542
			order[11] = 1213
			order[12] = 241
			order[13] = 242
			order[14] = 243
			order[15] = 244
			order[16] = 245
			order[17] = 246
			order[18] = 256
			order[19] = 595
			order[20] = 592
			order[21] = 593
			order[22] = 594
			order[23] = 247
			order[24] = 316
			order[25] = 941
			order[26] = 317
			order[27] = 436
			order[28] = 998
			order[29] = 1423
			order[30] = 1424
			order[31] = 1425
			order[32] = 1000
			order[33] = 1419
			order[34] = 435
			order[35] = 308
			order[36] = 306
			order[37] = 362
			order[38] = 363
			order[39] = 307
			order[40] = 364
			order[41] = 365
			order[42] = 877
			order[43] = 878
			order[44] = 972
			order[45] = 318
			order[46] = 879
			order[47] = 975
			order[48] = 973
			order[49] = 974
			order[50] = 810
			order[51] = 882
			order[52] = 883
			order[53] = 884
			order[54] = 885
			order[55] = 886
			order[56] = 1044
			order[57] = 1045
			order[58] = 1046
			order[59] = 1038
			order[60] = 1039
			order[61] = 315
			order[62] = 1437
			order[63] = 1441
			order[64] = 1453
			order[65] = 1454
			order[66] = 1455
			order[67] = 1456
			order[68] = 1459
			order[69] = 1460
			order[70] = 367
			order[71] = 304
			order[72] = 893
			order[73] = 295
			order[74] = 0
			fix.Group.__init__(self, 296, 302, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

		class NoQuoteEntries(fix.Group):
			def __init__(self):
				order = fix.IntArray(110)
				order[0] = 299
				order[1] = 55
				order[2] = 65
				order[3] = 48
				order[4] = 22
				order[5] = 460
				order[6] = 1227
				order[7] = 1151
				order[8] = 461
				order[9] = 167
				order[10] = 762
				order[11] = 200
				order[12] = 541
				order[13] = 1079
				order[14] = 966
				order[15] = 1049
				order[16] = 965
				order[17] = 224
				order[18] = 225
				order[19] = 239
				order[20] = 226
				order[21] = 227
				order[22] = 228
				order[23] = 255
				order[24] = 543
				order[25] = 470
				order[26] = 471
				order[27] = 472
				order[28] = 240
				order[29] = 202
				order[30] = 947
				order[31] = 967
				order[32] = 968
				order[33] = 206
				order[34] = 231
				order[35] = 969
				order[36] = 1146
				order[37] = 996
				order[38] = 1147
				order[39] = 1191
				order[40] = 1192
				order[41] = 1193
				order[42] = 1194
				order[43] = 1195
				order[44] = 1196
				order[45] = 1197
				order[46] = 1198
				order[47] = 1199
				order[48] = 1200
				order[49] = 201
				order[50] = 1244
				order[51] = 1242
				order[52] = 997
				order[53] = 223
				order[54] = 207
				order[55] = 970
				order[56] = 971
				order[57] = 106
				order[58] = 348
				order[59] = 349
				order[60] = 107
				order[61] = 350
				order[62] = 351
				order[63] = 691
				order[64] = 667
				order[65] = 875
				order[66] = 876
				order[67] = 873
				order[68] = 874
				order[69] = 1435
				order[70] = 1439
				order[71] = 1449
				order[72] = 1450
				order[73] = 1451
				order[74] = 1452
				order[75] = 1457
				order[76] = 1458
				order[77] = 1478
				order[78] = 1479
				order[79] = 1480
				order[80] = 1481
				order[81] = 1482
				order[82] = 555
				order[83] = 132
				order[84] = 133
				order[85] = 134
				order[86] = 135
				order[87] = 62
				order[88] = 188
				order[89] = 190
				order[90] = 189
				order[91] = 191
				order[92] = 631
				order[93] = 632
				order[94] = 633
				order[95] = 634
				order[96] = 60
				order[97] = 336
				order[98] = 625
				order[99] = 64
				order[100] = 40
				order[101] = 193
				order[102] = 192
				order[103] = 642
				order[104] = 643
				order[105] = 15
				order[106] = 775
				order[107] = 528
				order[108] = 529
				order[109] = 0
				fix.Group.__init__(self, 295, 299, order)

			class NoSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 455
					order[1] = 456
					order[2] = 0
					fix.Group.__init__(self, 454, 455, order)

			class NoEvents(fix.Group):
				def __init__(self):
					order = fix.IntArray(6)
					order[0] = 865
					order[1] = 866
					order[2] = 1145
					order[3] = 867
					order[4] = 868
					order[5] = 0
					fix.Group.__init__(self, 864, 865, order)

			class NoInstrumentParties(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 1019
					order[1] = 1050
					order[2] = 1051
					order[3] = 1052
					order[4] = 0
					fix.Group.__init__(self, 1018, 1019, order)

				class NoInstrumentPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1053
						order[1] = 1054
						order[2] = 0
						fix.Group.__init__(self, 1052, 1053, order)

			class NoComplexEvents(fix.Group):
				def __init__(self):
					order = fix.IntArray(9)
					order[0] = 1484
					order[1] = 1485
					order[2] = 1486
					order[3] = 1487
					order[4] = 1488
					order[5] = 1489
					order[6] = 1490
					order[7] = 1491
					order[8] = 0
					fix.Group.__init__(self, 1483, 1484, order)

				class NoComplexEventDates(fix.Group):
					def __init__(self):
						order = fix.IntArray(4)
						order[0] = 1492
						order[1] = 1493
						order[2] = 1494
						order[3] = 0
						fix.Group.__init__(self, 1491, 1492, order)

					class NoComplexEventTimes(fix.Group):
						def __init__(self):
							order = fix.IntArray(3)
							order[0] = 1495
							order[1] = 1496
							order[2] = 0
							fix.Group.__init__(self, 1494, 1495, order)

			class NoLegs(fix.Group):
				def __init__(self):
					order = fix.IntArray(56)
					order[0] = 600
					order[1] = 601
					order[2] = 602
					order[3] = 603
					order[4] = 1788
					order[5] = 607
					order[6] = 608
					order[7] = 609
					order[8] = 764
					order[9] = 610
					order[10] = 611
					order[11] = 1212
					order[12] = 248
					order[13] = 249
					order[14] = 250
					order[15] = 251
					order[16] = 252
					order[17] = 253
					order[18] = 257
					order[19] = 599
					order[20] = 596
					order[21] = 597
					order[22] = 598
					order[23] = 254
					order[24] = 612
					order[25] = 942
					order[26] = 613
					order[27] = 614
					order[28] = 999
					order[29] = 1224
					order[30] = 1421
					order[31] = 1422
					order[32] = 1001
					order[33] = 1420
					order[34] = 615
					order[35] = 616
					order[36] = 617
					order[37] = 618
					order[38] = 619
					order[39] = 620
					order[40] = 621
					order[41] = 622
					order[42] = 623
					order[43] = 624
					order[44] = 556
					order[45] = 740
					order[46] = 739
					order[47] = 955
					order[48] = 956
					order[49] = 1358
					order[50] = 1017
					order[51] = 1436
					order[52] = 1440
					order[53] = 22041
					order[54] = 22049
					order[55] = 0
					fix.Group.__init__(self, 555, 600, order)

				class NoLegSecurityAltID(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 605
						order[1] = 606
						order[2] = 0
						fix.Group.__init__(self, 604, 605, order)

class BusinessMessageReject(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("j") )

class BidRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("k") )

	class NoBidDescriptors(fix.Group):
		def __init__(self):
			order = fix.IntArray(12)
			order[0] = 399
			order[1] = 400
			order[2] = 401
			order[3] = 404
			order[4] = 441
			order[5] = 402
			order[6] = 403
			order[7] = 405
			order[8] = 406
			order[9] = 407
			order[10] = 408
			order[11] = 0
			fix.Group.__init__(self, 398, 399, order)

	class NoBidComponents(fix.Group):
		def __init__(self):
			order = fix.IntArray(10)
			order[0] = 66
			order[1] = 54
			order[2] = 336
			order[3] = 625
			order[4] = 430
			order[5] = 63
			order[6] = 64
			order[7] = 1
			order[8] = 660
			order[9] = 0
			fix.Group.__init__(self, 420, 66, order)

class BidResponse(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("l") )

	class NoBidComponents(fix.Group):
		def __init__(self):
			order = fix.IntArray(19)
			order[0] = 12
			order[1] = 13
			order[2] = 479
			order[3] = 497
			order[4] = 66
			order[5] = 421
			order[6] = 54
			order[7] = 44
			order[8] = 423
			order[9] = 406
			order[10] = 430
			order[11] = 63
			order[12] = 64
			order[13] = 336
			order[14] = 625
			order[15] = 58
			order[16] = 354
			order[17] = 355
			order[18] = 0
			fix.Group.__init__(self, 420, 12, order)

class ListStrikePrice(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("m") )

	class NoStrikes(fix.Group):
		def __init__(self):
			order = fix.IntArray(92)
			order[0] = 55
			order[1] = 65
			order[2] = 48
			order[3] = 22
			order[4] = 460
			order[5] = 1227
			order[6] = 1151
			order[7] = 461
			order[8] = 167
			order[9] = 762
			order[10] = 200
			order[11] = 541
			order[12] = 1079
			order[13] = 966
			order[14] = 1049
			order[15] = 965
			order[16] = 224
			order[17] = 225
			order[18] = 239
			order[19] = 226
			order[20] = 227
			order[21] = 228
			order[22] = 255
			order[23] = 543
			order[24] = 470
			order[25] = 471
			order[26] = 472
			order[27] = 240
			order[28] = 202
			order[29] = 947
			order[30] = 967
			order[31] = 968
			order[32] = 206
			order[33] = 231
			order[34] = 969
			order[35] = 1146
			order[36] = 996
			order[37] = 1147
			order[38] = 1191
			order[39] = 1192
			order[40] = 1193
			order[41] = 1194
			order[42] = 1195
			order[43] = 1196
			order[44] = 1197
			order[45] = 1198
			order[46] = 1199
			order[47] = 1200
			order[48] = 201
			order[49] = 1244
			order[50] = 1242
			order[51] = 997
			order[52] = 223
			order[53] = 207
			order[54] = 970
			order[55] = 971
			order[56] = 106
			order[57] = 348
			order[58] = 349
			order[59] = 107
			order[60] = 350
			order[61] = 351
			order[62] = 691
			order[63] = 667
			order[64] = 875
			order[65] = 876
			order[66] = 873
			order[67] = 874
			order[68] = 1435
			order[69] = 1439
			order[70] = 1449
			order[71] = 1450
			order[72] = 1451
			order[73] = 1452
			order[74] = 1457
			order[75] = 1458
			order[76] = 1478
			order[77] = 1479
			order[78] = 1480
			order[79] = 1481
			order[80] = 1482
			order[81] = 711
			order[82] = 140
			order[83] = 11
			order[84] = 526
			order[85] = 54
			order[86] = 44
			order[87] = 15
			order[88] = 58
			order[89] = 354
			order[90] = 355
			order[91] = 0
			fix.Group.__init__(self, 428, 55, order)

		class NoSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 455
				order[1] = 456
				order[2] = 0
				fix.Group.__init__(self, 454, 455, order)

		class NoEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 865
				order[1] = 866
				order[2] = 1145
				order[3] = 867
				order[4] = 868
				order[5] = 0
				fix.Group.__init__(self, 864, 865, order)

		class NoInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1019
				order[1] = 1050
				order[2] = 1051
				order[3] = 1052
				order[4] = 0
				fix.Group.__init__(self, 1018, 1019, order)

			class NoInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1053
					order[1] = 1054
					order[2] = 0
					fix.Group.__init__(self, 1052, 1053, order)

		class NoComplexEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(9)
				order[0] = 1484
				order[1] = 1485
				order[2] = 1486
				order[3] = 1487
				order[4] = 1488
				order[5] = 1489
				order[6] = 1490
				order[7] = 1491
				order[8] = 0
				fix.Group.__init__(self, 1483, 1484, order)

			class NoComplexEventDates(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1492
					order[1] = 1493
					order[2] = 1494
					order[3] = 0
					fix.Group.__init__(self, 1491, 1492, order)

				class NoComplexEventTimes(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1495
						order[1] = 1496
						order[2] = 0
						fix.Group.__init__(self, 1494, 1495, order)

		class NoUnderlyings(fix.Group):
			def __init__(self):
				order = fix.IntArray(70)
				order[0] = 311
				order[1] = 312
				order[2] = 309
				order[3] = 305
				order[4] = 462
				order[5] = 463
				order[6] = 310
				order[7] = 763
				order[8] = 313
				order[9] = 542
				order[10] = 1213
				order[11] = 241
				order[12] = 242
				order[13] = 243
				order[14] = 244
				order[15] = 245
				order[16] = 246
				order[17] = 256
				order[18] = 595
				order[19] = 592
				order[20] = 593
				order[21] = 594
				order[22] = 247
				order[23] = 316
				order[24] = 941
				order[25] = 317
				order[26] = 436
				order[27] = 998
				order[28] = 1423
				order[29] = 1424
				order[30] = 1425
				order[31] = 1000
				order[32] = 1419
				order[33] = 435
				order[34] = 308
				order[35] = 306
				order[36] = 362
				order[37] = 363
				order[38] = 307
				order[39] = 364
				order[40] = 365
				order[41] = 877
				order[42] = 878
				order[43] = 972
				order[44] = 318
				order[45] = 879
				order[46] = 975
				order[47] = 973
				order[48] = 974
				order[49] = 810
				order[50] = 882
				order[51] = 883
				order[52] = 884
				order[53] = 885
				order[54] = 886
				order[55] = 1044
				order[56] = 1045
				order[57] = 1046
				order[58] = 1038
				order[59] = 1039
				order[60] = 315
				order[61] = 1437
				order[62] = 1441
				order[63] = 1453
				order[64] = 1454
				order[65] = 1455
				order[66] = 1456
				order[67] = 1459
				order[68] = 1460
				order[69] = 0
				fix.Group.__init__(self, 711, 311, order)

			class NoUnderlyingSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 458
					order[1] = 459
					order[2] = 0
					fix.Group.__init__(self, 457, 458, order)

			class NoUnderlyingStips(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 888
					order[1] = 889
					order[2] = 0
					fix.Group.__init__(self, 887, 888, order)

			class NoUndlyInstrumentParties(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 1059
					order[1] = 1060
					order[2] = 1061
					order[3] = 1062
					order[4] = 0
					fix.Group.__init__(self, 1058, 1059, order)

				class NoUndlyInstrumentPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1063
						order[1] = 1064
						order[2] = 0
						fix.Group.__init__(self, 1062, 1063, order)

class RegistrationInstructions(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("o") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoRegistDtls(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 509
			order[1] = 511
			order[2] = 474
			order[3] = 482
			order[4] = 539
			order[5] = 522
			order[6] = 486
			order[7] = 475
			order[8] = 0
			fix.Group.__init__(self, 473, 509, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

	class NoDistribInsts(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 477
			order[1] = 512
			order[2] = 478
			order[3] = 498
			order[4] = 499
			order[5] = 500
			order[6] = 501
			order[7] = 502
			order[8] = 0
			fix.Group.__init__(self, 510, 477, order)

class RegistrationInstructionsResponse(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("p") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

class OrderMassCancelRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("q") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyingSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 458
			order[1] = 459
			order[2] = 0
			fix.Group.__init__(self, 457, 458, order)

	class NoUnderlyingStips(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 888
			order[1] = 889
			order[2] = 0
			fix.Group.__init__(self, 887, 888, order)

	class NoUndlyInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1059
			order[1] = 1060
			order[2] = 1061
			order[3] = 1062
			order[4] = 0
			fix.Group.__init__(self, 1058, 1059, order)

		class NoUndlyInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1063
				order[1] = 1064
				order[2] = 0
				fix.Group.__init__(self, 1062, 1063, order)

	class NoTargetPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1462
			order[1] = 1463
			order[2] = 1464
			order[3] = 0
			fix.Group.__init__(self, 1461, 1462, order)

class OrderMassCancelReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("r") )

	class NoAffectedOrders(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 41
			order[1] = 535
			order[2] = 536
			order[3] = 0
			fix.Group.__init__(self, 534, 41, order)

	class NoNotAffectedOrders(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 1372
			order[1] = 1371
			order[2] = 0
			fix.Group.__init__(self, 1370, 1372, order)

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyingSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 458
			order[1] = 459
			order[2] = 0
			fix.Group.__init__(self, 457, 458, order)

	class NoUnderlyingStips(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 888
			order[1] = 889
			order[2] = 0
			fix.Group.__init__(self, 887, 888, order)

	class NoUndlyInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1059
			order[1] = 1060
			order[2] = 1061
			order[3] = 1062
			order[4] = 0
			fix.Group.__init__(self, 1058, 1059, order)

		class NoUndlyInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1063
				order[1] = 1064
				order[2] = 0
				fix.Group.__init__(self, 1062, 1063, order)

	class NoTargetPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1462
			order[1] = 1463
			order[2] = 1464
			order[3] = 0
			fix.Group.__init__(self, 1461, 1462, order)

class NewOrderCross(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("s") )

	class NoRootPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1117
			order[1] = 1118
			order[2] = 1119
			order[3] = 1120
			order[4] = 0
			fix.Group.__init__(self, 1116, 1117, order)

		class NoRootPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1121
				order[1] = 1122
				order[2] = 0
				fix.Group.__init__(self, 1120, 1121, order)

	class NoSides(fix.Group):
		def __init__(self):
			order = fix.IntArray(44)
			order[0] = 54
			order[1] = 41
			order[2] = 11
			order[3] = 526
			order[4] = 583
			order[5] = 453
			order[6] = 229
			order[7] = 75
			order[8] = 1
			order[9] = 660
			order[10] = 581
			order[11] = 589
			order[12] = 590
			order[13] = 591
			order[14] = 70
			order[15] = 78
			order[16] = 854
			order[17] = 38
			order[18] = 152
			order[19] = 516
			order[20] = 468
			order[21] = 469
			order[22] = 12
			order[23] = 13
			order[24] = 479
			order[25] = 497
			order[26] = 528
			order[27] = 529
			order[28] = 1091
			order[29] = 582
			order[30] = 121
			order[31] = 120
			order[32] = 775
			order[33] = 58
			order[34] = 354
			order[35] = 355
			order[36] = 77
			order[37] = 203
			order[38] = 544
			order[39] = 635
			order[40] = 377
			order[41] = 659
			order[42] = 962
			order[43] = 0
			fix.Group.__init__(self, 552, 54, order)

		class NoPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 448
				order[1] = 447
				order[2] = 452
				order[3] = 2376
				order[4] = 802
				order[5] = 0
				fix.Group.__init__(self, 453, 448, order)

			class NoPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 523
					order[1] = 803
					order[2] = 0
					fix.Group.__init__(self, 802, 523, order)

		class NoAllocs(fix.Group):
			def __init__(self):
				order = fix.IntArray(7)
				order[0] = 79
				order[1] = 661
				order[2] = 736
				order[3] = 467
				order[4] = 539
				order[5] = 80
				order[6] = 0
				fix.Group.__init__(self, 78, 79, order)

			class NoNestedPartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 524
					order[1] = 525
					order[2] = 538
					order[3] = 804
					order[4] = 0
					fix.Group.__init__(self, 539, 524, order)

				class NoNestedPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 545
						order[1] = 805
						order[2] = 0
						fix.Group.__init__(self, 804, 545, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoTradingSessions(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 336
			order[1] = 625
			order[2] = 0
			fix.Group.__init__(self, 386, 336, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoStrategyParameters(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 958
			order[1] = 959
			order[2] = 960
			order[3] = 0
			fix.Group.__init__(self, 957, 958, order)

class CrossOrderCancelReplaceRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("t") )

	class NoRootPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1117
			order[1] = 1118
			order[2] = 1119
			order[3] = 1120
			order[4] = 0
			fix.Group.__init__(self, 1116, 1117, order)

		class NoRootPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1121
				order[1] = 1122
				order[2] = 0
				fix.Group.__init__(self, 1120, 1121, order)

	class NoSides(fix.Group):
		def __init__(self):
			order = fix.IntArray(44)
			order[0] = 54
			order[1] = 41
			order[2] = 11
			order[3] = 526
			order[4] = 583
			order[5] = 453
			order[6] = 229
			order[7] = 75
			order[8] = 1
			order[9] = 660
			order[10] = 581
			order[11] = 589
			order[12] = 590
			order[13] = 591
			order[14] = 70
			order[15] = 78
			order[16] = 854
			order[17] = 38
			order[18] = 152
			order[19] = 516
			order[20] = 468
			order[21] = 469
			order[22] = 12
			order[23] = 13
			order[24] = 479
			order[25] = 497
			order[26] = 528
			order[27] = 529
			order[28] = 1091
			order[29] = 582
			order[30] = 121
			order[31] = 120
			order[32] = 775
			order[33] = 58
			order[34] = 354
			order[35] = 355
			order[36] = 77
			order[37] = 203
			order[38] = 544
			order[39] = 635
			order[40] = 377
			order[41] = 659
			order[42] = 962
			order[43] = 0
			fix.Group.__init__(self, 552, 54, order)

		class NoPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 448
				order[1] = 447
				order[2] = 452
				order[3] = 2376
				order[4] = 802
				order[5] = 0
				fix.Group.__init__(self, 453, 448, order)

			class NoPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 523
					order[1] = 803
					order[2] = 0
					fix.Group.__init__(self, 802, 523, order)

		class NoAllocs(fix.Group):
			def __init__(self):
				order = fix.IntArray(7)
				order[0] = 79
				order[1] = 661
				order[2] = 736
				order[3] = 467
				order[4] = 539
				order[5] = 80
				order[6] = 0
				fix.Group.__init__(self, 78, 79, order)

			class NoNestedPartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 524
					order[1] = 525
					order[2] = 538
					order[3] = 804
					order[4] = 0
					fix.Group.__init__(self, 539, 524, order)

				class NoNestedPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 545
						order[1] = 805
						order[2] = 0
						fix.Group.__init__(self, 804, 545, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoTradingSessions(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 336
			order[1] = 625
			order[2] = 0
			fix.Group.__init__(self, 386, 336, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoStrategyParameters(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 958
			order[1] = 959
			order[2] = 960
			order[3] = 0
			fix.Group.__init__(self, 957, 958, order)

class CrossOrderCancelRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("u") )

	class NoRootPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1117
			order[1] = 1118
			order[2] = 1119
			order[3] = 1120
			order[4] = 0
			fix.Group.__init__(self, 1116, 1117, order)

		class NoRootPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1121
				order[1] = 1122
				order[2] = 0
				fix.Group.__init__(self, 1120, 1121, order)

	class NoSides(fix.Group):
		def __init__(self):
			order = fix.IntArray(19)
			order[0] = 54
			order[1] = 41
			order[2] = 11
			order[3] = 526
			order[4] = 583
			order[5] = 586
			order[6] = 453
			order[7] = 229
			order[8] = 75
			order[9] = 38
			order[10] = 152
			order[11] = 516
			order[12] = 468
			order[13] = 469
			order[14] = 376
			order[15] = 58
			order[16] = 354
			order[17] = 355
			order[18] = 0
			fix.Group.__init__(self, 552, 54, order)

		class NoPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 448
				order[1] = 447
				order[2] = 452
				order[3] = 2376
				order[4] = 802
				order[5] = 0
				fix.Group.__init__(self, 453, 448, order)

			class NoPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 523
					order[1] = 803
					order[2] = 0
					fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

class SecurityTypeRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("v") )

class SecurityTypes(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("w") )

	class NoSecurityTypes(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 167
			order[1] = 762
			order[2] = 460
			order[3] = 461
			order[4] = 60
			order[5] = 0
			fix.Group.__init__(self, 558, 167, order)

class SecurityListRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("x") )

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoInstrAttrib(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 871
			order[1] = 872
			order[2] = 0
			fix.Group.__init__(self, 870, 871, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

class SecurityList(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("y") )

	class NoRelatedSym(fix.Group):
		def __init__(self):
			order = fix.IntArray(117)
			order[0] = 55
			order[1] = 65
			order[2] = 48
			order[3] = 22
			order[4] = 460
			order[5] = 1227
			order[6] = 1151
			order[7] = 461
			order[8] = 167
			order[9] = 762
			order[10] = 200
			order[11] = 541
			order[12] = 1079
			order[13] = 966
			order[14] = 1049
			order[15] = 965
			order[16] = 224
			order[17] = 225
			order[18] = 239
			order[19] = 226
			order[20] = 227
			order[21] = 228
			order[22] = 255
			order[23] = 543
			order[24] = 470
			order[25] = 471
			order[26] = 472
			order[27] = 240
			order[28] = 202
			order[29] = 947
			order[30] = 967
			order[31] = 968
			order[32] = 206
			order[33] = 231
			order[34] = 969
			order[35] = 1146
			order[36] = 996
			order[37] = 1147
			order[38] = 1191
			order[39] = 1192
			order[40] = 1193
			order[41] = 1194
			order[42] = 1195
			order[43] = 1196
			order[44] = 1197
			order[45] = 1198
			order[46] = 1199
			order[47] = 1200
			order[48] = 201
			order[49] = 1244
			order[50] = 1242
			order[51] = 997
			order[52] = 223
			order[53] = 207
			order[54] = 970
			order[55] = 971
			order[56] = 106
			order[57] = 348
			order[58] = 349
			order[59] = 107
			order[60] = 350
			order[61] = 351
			order[62] = 691
			order[63] = 667
			order[64] = 875
			order[65] = 876
			order[66] = 873
			order[67] = 874
			order[68] = 1435
			order[69] = 1439
			order[70] = 1449
			order[71] = 1450
			order[72] = 1451
			order[73] = 1452
			order[74] = 1457
			order[75] = 1458
			order[76] = 1478
			order[77] = 1479
			order[78] = 1480
			order[79] = 1481
			order[80] = 1482
			order[81] = 668
			order[82] = 869
			order[83] = 913
			order[84] = 914
			order[85] = 915
			order[86] = 918
			order[87] = 788
			order[88] = 916
			order[89] = 917
			order[90] = 919
			order[91] = 898
			order[92] = 1201
			order[93] = 711
			order[94] = 15
			order[95] = 232
			order[96] = 555
			order[97] = 218
			order[98] = 22048
			order[99] = 220
			order[100] = 221
			order[101] = 222
			order[102] = 662
			order[103] = 663
			order[104] = 699
			order[105] = 761
			order[106] = 235
			order[107] = 236
			order[108] = 701
			order[109] = 696
			order[110] = 697
			order[111] = 698
			order[112] = 58
			order[113] = 354
			order[114] = 355
			order[115] = 1504
			order[116] = 0
			fix.Group.__init__(self, 146, 55, order)

		class NoSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 455
				order[1] = 456
				order[2] = 0
				fix.Group.__init__(self, 454, 455, order)

		class NoEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 865
				order[1] = 866
				order[2] = 1145
				order[3] = 867
				order[4] = 868
				order[5] = 0
				fix.Group.__init__(self, 864, 865, order)

		class NoInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1019
				order[1] = 1050
				order[2] = 1051
				order[3] = 1052
				order[4] = 0
				fix.Group.__init__(self, 1018, 1019, order)

			class NoInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1053
					order[1] = 1054
					order[2] = 0
					fix.Group.__init__(self, 1052, 1053, order)

		class NoComplexEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(9)
				order[0] = 1484
				order[1] = 1485
				order[2] = 1486
				order[3] = 1487
				order[4] = 1488
				order[5] = 1489
				order[6] = 1490
				order[7] = 1491
				order[8] = 0
				fix.Group.__init__(self, 1483, 1484, order)

			class NoComplexEventDates(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1492
					order[1] = 1493
					order[2] = 1494
					order[3] = 0
					fix.Group.__init__(self, 1491, 1492, order)

				class NoComplexEventTimes(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1495
						order[1] = 1496
						order[2] = 0
						fix.Group.__init__(self, 1494, 1495, order)

		class NoInstrAttrib(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 871
				order[1] = 872
				order[2] = 0
				fix.Group.__init__(self, 870, 871, order)

		class NoTickRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1206
				order[1] = 1207
				order[2] = 1208
				order[3] = 1209
				order[4] = 0
				fix.Group.__init__(self, 1205, 1206, order)

		class NoLotTypeRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1093
				order[1] = 1231
				order[2] = 0
				fix.Group.__init__(self, 1234, 1093, order)

		class NoTradingSessionRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 336
				order[1] = 625
				order[2] = 0
				fix.Group.__init__(self, 1309, 336, order)

			class NoOrdTypeRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 40
					order[1] = 0
					fix.Group.__init__(self, 1237, 40, order)

			class NoTimeInForceRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 59
					order[1] = 0
					fix.Group.__init__(self, 1239, 59, order)

			class NoExecInstRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 1308
					order[1] = 0
					fix.Group.__init__(self, 1232, 1308, order)

			class NoMatchRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1142
					order[1] = 574
					order[2] = 0
					fix.Group.__init__(self, 1235, 1142, order)

			class NoMDFeedTypes(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1022
					order[1] = 264
					order[2] = 1021
					order[3] = 0
					fix.Group.__init__(self, 1141, 1022, order)

		class NoNestedInstrAttrib(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1210
				order[1] = 1211
				order[2] = 0
				fix.Group.__init__(self, 1312, 1210, order)

		class NoStrikeRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(7)
				order[0] = 1223
				order[1] = 1202
				order[2] = 1203
				order[3] = 1204
				order[4] = 1304
				order[5] = 1236
				order[6] = 0
				fix.Group.__init__(self, 1201, 1223, order)

			class NoMaturityRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(7)
					order[0] = 1222
					order[1] = 1303
					order[2] = 1302
					order[3] = 1241
					order[4] = 1226
					order[5] = 1229
					order[6] = 0
					fix.Group.__init__(self, 1236, 1222, order)

		class NoUnderlyings(fix.Group):
			def __init__(self):
				order = fix.IntArray(70)
				order[0] = 311
				order[1] = 312
				order[2] = 309
				order[3] = 305
				order[4] = 462
				order[5] = 463
				order[6] = 310
				order[7] = 763
				order[8] = 313
				order[9] = 542
				order[10] = 1213
				order[11] = 241
				order[12] = 242
				order[13] = 243
				order[14] = 244
				order[15] = 245
				order[16] = 246
				order[17] = 256
				order[18] = 595
				order[19] = 592
				order[20] = 593
				order[21] = 594
				order[22] = 247
				order[23] = 316
				order[24] = 941
				order[25] = 317
				order[26] = 436
				order[27] = 998
				order[28] = 1423
				order[29] = 1424
				order[30] = 1425
				order[31] = 1000
				order[32] = 1419
				order[33] = 435
				order[34] = 308
				order[35] = 306
				order[36] = 362
				order[37] = 363
				order[38] = 307
				order[39] = 364
				order[40] = 365
				order[41] = 877
				order[42] = 878
				order[43] = 972
				order[44] = 318
				order[45] = 879
				order[46] = 975
				order[47] = 973
				order[48] = 974
				order[49] = 810
				order[50] = 882
				order[51] = 883
				order[52] = 884
				order[53] = 885
				order[54] = 886
				order[55] = 1044
				order[56] = 1045
				order[57] = 1046
				order[58] = 1038
				order[59] = 1039
				order[60] = 315
				order[61] = 1437
				order[62] = 1441
				order[63] = 1453
				order[64] = 1454
				order[65] = 1455
				order[66] = 1456
				order[67] = 1459
				order[68] = 1460
				order[69] = 0
				fix.Group.__init__(self, 711, 311, order)

			class NoUnderlyingSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 458
					order[1] = 459
					order[2] = 0
					fix.Group.__init__(self, 457, 458, order)

			class NoUnderlyingStips(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 888
					order[1] = 889
					order[2] = 0
					fix.Group.__init__(self, 887, 888, order)

			class NoUndlyInstrumentParties(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 1059
					order[1] = 1060
					order[2] = 1061
					order[3] = 1062
					order[4] = 0
					fix.Group.__init__(self, 1058, 1059, order)

				class NoUndlyInstrumentPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1063
						order[1] = 1064
						order[2] = 0
						fix.Group.__init__(self, 1062, 1063, order)

		class NoStipulations(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 233
				order[1] = 234
				order[2] = 0
				fix.Group.__init__(self, 232, 233, order)

		class NoLegs(fix.Group):
			def __init__(self):
				order = fix.IntArray(64)
				order[0] = 600
				order[1] = 601
				order[2] = 602
				order[3] = 603
				order[4] = 1788
				order[5] = 607
				order[6] = 608
				order[7] = 609
				order[8] = 764
				order[9] = 610
				order[10] = 611
				order[11] = 1212
				order[12] = 248
				order[13] = 249
				order[14] = 250
				order[15] = 251
				order[16] = 252
				order[17] = 253
				order[18] = 257
				order[19] = 599
				order[20] = 596
				order[21] = 597
				order[22] = 598
				order[23] = 254
				order[24] = 612
				order[25] = 942
				order[26] = 613
				order[27] = 614
				order[28] = 999
				order[29] = 1224
				order[30] = 1421
				order[31] = 1422
				order[32] = 1001
				order[33] = 1420
				order[34] = 615
				order[35] = 616
				order[36] = 617
				order[37] = 618
				order[38] = 619
				order[39] = 620
				order[40] = 621
				order[41] = 622
				order[42] = 623
				order[43] = 624
				order[44] = 556
				order[45] = 740
				order[46] = 739
				order[47] = 955
				order[48] = 956
				order[49] = 1358
				order[50] = 1017
				order[51] = 1436
				order[52] = 1440
				order[53] = 22041
				order[54] = 22049
				order[55] = 690
				order[56] = 587
				order[57] = 683
				order[58] = 676
				order[59] = 677
				order[60] = 678
				order[61] = 679
				order[62] = 680
				order[63] = 0
				fix.Group.__init__(self, 555, 600, order)

			class NoLegSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 605
					order[1] = 606
					order[2] = 0
					fix.Group.__init__(self, 604, 605, order)

			class NoLegStipulations(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 688
					order[1] = 689
					order[2] = 0
					fix.Group.__init__(self, 683, 688, order)

class DerivativeSecurityListRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("z") )

	class NoUnderlyingSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 458
			order[1] = 459
			order[2] = 0
			fix.Group.__init__(self, 457, 458, order)

	class NoUnderlyingStips(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 888
			order[1] = 889
			order[2] = 0
			fix.Group.__init__(self, 887, 888, order)

	class NoUndlyInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1059
			order[1] = 1060
			order[2] = 1061
			order[3] = 1062
			order[4] = 0
			fix.Group.__init__(self, 1058, 1059, order)

		class NoUndlyInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1063
				order[1] = 1064
				order[2] = 0
				fix.Group.__init__(self, 1062, 1063, order)

	class NoDerivativeSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 1219
			order[1] = 1220
			order[2] = 0
			fix.Group.__init__(self, 1218, 1219, order)

	class NoDerivativeEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 1287
			order[1] = 1288
			order[2] = 1289
			order[3] = 1290
			order[4] = 1291
			order[5] = 0
			fix.Group.__init__(self, 1286, 1287, order)

	class NoDerivativeInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1293
			order[1] = 1294
			order[2] = 1295
			order[3] = 1296
			order[4] = 0
			fix.Group.__init__(self, 1292, 1293, order)

		class NoDerivativeInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1297
				order[1] = 1298
				order[2] = 0
				fix.Group.__init__(self, 1296, 1297, order)

class DerivativeSecurityList(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AA") )

	class NoUnderlyingSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 458
			order[1] = 459
			order[2] = 0
			fix.Group.__init__(self, 457, 458, order)

	class NoUnderlyingStips(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 888
			order[1] = 889
			order[2] = 0
			fix.Group.__init__(self, 887, 888, order)

	class NoUndlyInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1059
			order[1] = 1060
			order[2] = 1061
			order[3] = 1062
			order[4] = 0
			fix.Group.__init__(self, 1058, 1059, order)

		class NoUndlyInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1063
				order[1] = 1064
				order[2] = 0
				fix.Group.__init__(self, 1062, 1063, order)

	class NoDerivativeSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 1219
			order[1] = 1220
			order[2] = 0
			fix.Group.__init__(self, 1218, 1219, order)

	class NoDerivativeEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 1287
			order[1] = 1288
			order[2] = 1289
			order[3] = 1290
			order[4] = 1291
			order[5] = 0
			fix.Group.__init__(self, 1286, 1287, order)

	class NoDerivativeInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1293
			order[1] = 1294
			order[2] = 1295
			order[3] = 1296
			order[4] = 0
			fix.Group.__init__(self, 1292, 1293, order)

		class NoDerivativeInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1297
				order[1] = 1298
				order[2] = 0
				fix.Group.__init__(self, 1296, 1297, order)

	class NoDerivativeInstrAttrib(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 1313
			order[1] = 1314
			order[2] = 0
			fix.Group.__init__(self, 1311, 1313, order)

	class NoMarketSegments(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1301
			order[1] = 1300
			order[2] = 1201
			order[3] = 0
			fix.Group.__init__(self, 1310, 1301, order)

		class NoTickRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1206
				order[1] = 1207
				order[2] = 1208
				order[3] = 1209
				order[4] = 0
				fix.Group.__init__(self, 1205, 1206, order)

		class NoLotTypeRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1093
				order[1] = 1231
				order[2] = 0
				fix.Group.__init__(self, 1234, 1093, order)

		class NoTradingSessionRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 336
				order[1] = 625
				order[2] = 0
				fix.Group.__init__(self, 1309, 336, order)

			class NoOrdTypeRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 40
					order[1] = 0
					fix.Group.__init__(self, 1237, 40, order)

			class NoTimeInForceRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 59
					order[1] = 0
					fix.Group.__init__(self, 1239, 59, order)

			class NoExecInstRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 1308
					order[1] = 0
					fix.Group.__init__(self, 1232, 1308, order)

			class NoMatchRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1142
					order[1] = 574
					order[2] = 0
					fix.Group.__init__(self, 1235, 1142, order)

			class NoMDFeedTypes(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1022
					order[1] = 264
					order[2] = 1021
					order[3] = 0
					fix.Group.__init__(self, 1141, 1022, order)

		class NoNestedInstrAttrib(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1210
				order[1] = 1211
				order[2] = 0
				fix.Group.__init__(self, 1312, 1210, order)

		class NoStrikeRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(7)
				order[0] = 1223
				order[1] = 1202
				order[2] = 1203
				order[3] = 1204
				order[4] = 1304
				order[5] = 1236
				order[6] = 0
				fix.Group.__init__(self, 1201, 1223, order)

			class NoMaturityRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(7)
					order[0] = 1222
					order[1] = 1303
					order[2] = 1302
					order[3] = 1241
					order[4] = 1226
					order[5] = 1229
					order[6] = 0
					fix.Group.__init__(self, 1236, 1222, order)

	class NoRelatedSym(fix.Group):
		def __init__(self):
			order = fix.IntArray(95)
			order[0] = 55
			order[1] = 65
			order[2] = 48
			order[3] = 22
			order[4] = 460
			order[5] = 1227
			order[6] = 1151
			order[7] = 461
			order[8] = 167
			order[9] = 762
			order[10] = 200
			order[11] = 541
			order[12] = 1079
			order[13] = 966
			order[14] = 1049
			order[15] = 965
			order[16] = 224
			order[17] = 225
			order[18] = 239
			order[19] = 226
			order[20] = 227
			order[21] = 228
			order[22] = 255
			order[23] = 543
			order[24] = 470
			order[25] = 471
			order[26] = 472
			order[27] = 240
			order[28] = 202
			order[29] = 947
			order[30] = 967
			order[31] = 968
			order[32] = 206
			order[33] = 231
			order[34] = 969
			order[35] = 1146
			order[36] = 996
			order[37] = 1147
			order[38] = 1191
			order[39] = 1192
			order[40] = 1193
			order[41] = 1194
			order[42] = 1195
			order[43] = 1196
			order[44] = 1197
			order[45] = 1198
			order[46] = 1199
			order[47] = 1200
			order[48] = 201
			order[49] = 1244
			order[50] = 1242
			order[51] = 997
			order[52] = 223
			order[53] = 207
			order[54] = 970
			order[55] = 971
			order[56] = 106
			order[57] = 348
			order[58] = 349
			order[59] = 107
			order[60] = 350
			order[61] = 351
			order[62] = 691
			order[63] = 667
			order[64] = 875
			order[65] = 876
			order[66] = 873
			order[67] = 874
			order[68] = 1435
			order[69] = 1439
			order[70] = 1449
			order[71] = 1450
			order[72] = 1451
			order[73] = 1452
			order[74] = 1457
			order[75] = 1458
			order[76] = 1478
			order[77] = 1479
			order[78] = 1480
			order[79] = 1481
			order[80] = 1482
			order[81] = 1305
			order[82] = 1221
			order[83] = 1230
			order[84] = 1240
			order[85] = 15
			order[86] = 292
			order[87] = 668
			order[88] = 869
			order[89] = 555
			order[90] = 58
			order[91] = 354
			order[92] = 355
			order[93] = 1504
			order[94] = 0
			fix.Group.__init__(self, 146, 55, order)

		class NoSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 455
				order[1] = 456
				order[2] = 0
				fix.Group.__init__(self, 454, 455, order)

		class NoEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 865
				order[1] = 866
				order[2] = 1145
				order[3] = 867
				order[4] = 868
				order[5] = 0
				fix.Group.__init__(self, 864, 865, order)

		class NoInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1019
				order[1] = 1050
				order[2] = 1051
				order[3] = 1052
				order[4] = 0
				fix.Group.__init__(self, 1018, 1019, order)

			class NoInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1053
					order[1] = 1054
					order[2] = 0
					fix.Group.__init__(self, 1052, 1053, order)

		class NoComplexEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(9)
				order[0] = 1484
				order[1] = 1485
				order[2] = 1486
				order[3] = 1487
				order[4] = 1488
				order[5] = 1489
				order[6] = 1490
				order[7] = 1491
				order[8] = 0
				fix.Group.__init__(self, 1483, 1484, order)

			class NoComplexEventDates(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1492
					order[1] = 1493
					order[2] = 1494
					order[3] = 0
					fix.Group.__init__(self, 1491, 1492, order)

				class NoComplexEventTimes(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1495
						order[1] = 1496
						order[2] = 0
						fix.Group.__init__(self, 1494, 1495, order)

		class NoInstrAttrib(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 871
				order[1] = 872
				order[2] = 0
				fix.Group.__init__(self, 870, 871, order)

		class NoLegs(fix.Group):
			def __init__(self):
				order = fix.IntArray(56)
				order[0] = 600
				order[1] = 601
				order[2] = 602
				order[3] = 603
				order[4] = 1788
				order[5] = 607
				order[6] = 608
				order[7] = 609
				order[8] = 764
				order[9] = 610
				order[10] = 611
				order[11] = 1212
				order[12] = 248
				order[13] = 249
				order[14] = 250
				order[15] = 251
				order[16] = 252
				order[17] = 253
				order[18] = 257
				order[19] = 599
				order[20] = 596
				order[21] = 597
				order[22] = 598
				order[23] = 254
				order[24] = 612
				order[25] = 942
				order[26] = 613
				order[27] = 614
				order[28] = 999
				order[29] = 1224
				order[30] = 1421
				order[31] = 1422
				order[32] = 1001
				order[33] = 1420
				order[34] = 615
				order[35] = 616
				order[36] = 617
				order[37] = 618
				order[38] = 619
				order[39] = 620
				order[40] = 621
				order[41] = 622
				order[42] = 623
				order[43] = 624
				order[44] = 556
				order[45] = 740
				order[46] = 739
				order[47] = 955
				order[48] = 956
				order[49] = 1358
				order[50] = 1017
				order[51] = 1436
				order[52] = 1440
				order[53] = 22041
				order[54] = 22049
				order[55] = 0
				fix.Group.__init__(self, 555, 600, order)

			class NoLegSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 605
					order[1] = 606
					order[2] = 0
					fix.Group.__init__(self, 604, 605, order)

class NewOrderMultileg(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AB") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoAllocs(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 79
			order[1] = 661
			order[2] = 736
			order[3] = 467
			order[4] = 948
			order[5] = 80
			order[6] = 0
			fix.Group.__init__(self, 78, 79, order)

		class NoNested3PartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 949
				order[1] = 950
				order[2] = 951
				order[3] = 952
				order[4] = 0
				fix.Group.__init__(self, 948, 949, order)

			class NoNested3PartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 953
					order[1] = 954
					order[2] = 0
					fix.Group.__init__(self, 952, 953, order)

	class NoTradingSessions(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 336
			order[1] = 625
			order[2] = 0
			fix.Group.__init__(self, 386, 336, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(73)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 687
			order[56] = 690
			order[57] = 683
			order[58] = 1366
			order[59] = 670
			order[60] = 564
			order[61] = 565
			order[62] = 539
			order[63] = 654
			order[64] = 587
			order[65] = 588
			order[66] = 675
			order[67] = 685
			order[68] = 1379
			order[69] = 1381
			order[70] = 1383
			order[71] = 1384
			order[72] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

		class NoLegStipulations(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 688
				order[1] = 689
				order[2] = 0
				fix.Group.__init__(self, 683, 688, order)

		class NoLegAllocs(fix.Group):
			def __init__(self):
				order = fix.IntArray(7)
				order[0] = 671
				order[1] = 672
				order[2] = 756
				order[3] = 673
				order[4] = 674
				order[5] = 1367
				order[6] = 0
				fix.Group.__init__(self, 670, 671, order)

			class NoNested2PartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 757
					order[1] = 758
					order[2] = 759
					order[3] = 806
					order[4] = 0
					fix.Group.__init__(self, 756, 757, order)

				class NoNested2PartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 760
						order[1] = 807
						order[2] = 0
						fix.Group.__init__(self, 806, 760, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

	class NoStrategyParameters(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 958
			order[1] = 959
			order[2] = 960
			order[3] = 0
			fix.Group.__init__(self, 957, 958, order)

class MultilegOrderCancelReplace(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AC") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoAllocs(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 79
			order[1] = 661
			order[2] = 736
			order[3] = 467
			order[4] = 948
			order[5] = 80
			order[6] = 0
			fix.Group.__init__(self, 78, 79, order)

		class NoNested3PartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 949
				order[1] = 950
				order[2] = 951
				order[3] = 952
				order[4] = 0
				fix.Group.__init__(self, 948, 949, order)

			class NoNested3PartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 953
					order[1] = 954
					order[2] = 0
					fix.Group.__init__(self, 952, 953, order)

	class NoTradingSessions(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 336
			order[1] = 625
			order[2] = 0
			fix.Group.__init__(self, 386, 336, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(73)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 687
			order[56] = 690
			order[57] = 683
			order[58] = 1366
			order[59] = 670
			order[60] = 564
			order[61] = 565
			order[62] = 539
			order[63] = 654
			order[64] = 587
			order[65] = 588
			order[66] = 675
			order[67] = 685
			order[68] = 1379
			order[69] = 1381
			order[70] = 1383
			order[71] = 1384
			order[72] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

		class NoLegStipulations(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 688
				order[1] = 689
				order[2] = 0
				fix.Group.__init__(self, 683, 688, order)

		class NoLegAllocs(fix.Group):
			def __init__(self):
				order = fix.IntArray(7)
				order[0] = 671
				order[1] = 672
				order[2] = 756
				order[3] = 673
				order[4] = 674
				order[5] = 1367
				order[6] = 0
				fix.Group.__init__(self, 670, 671, order)

			class NoNested2PartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 757
					order[1] = 758
					order[2] = 759
					order[3] = 806
					order[4] = 0
					fix.Group.__init__(self, 756, 757, order)

				class NoNested2PartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 760
						order[1] = 807
						order[2] = 0
						fix.Group.__init__(self, 806, 760, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

	class NoStrategyParameters(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 958
			order[1] = 959
			order[2] = 960
			order[3] = 0
			fix.Group.__init__(self, 957, 958, order)

class TradeCaptureReportRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AD") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoInstrAttrib(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 871
			order[1] = 872
			order[2] = 0
			fix.Group.__init__(self, 870, 871, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoDates(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 75
			order[1] = 779
			order[2] = 60
			order[3] = 0
			fix.Group.__init__(self, 580, 75, order)

class TradeCaptureReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AE") )

	class NoRootPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1117
			order[1] = 1118
			order[2] = 1119
			order[3] = 1120
			order[4] = 0
			fix.Group.__init__(self, 1116, 1117, order)

		class NoRootPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1121
				order[1] = 1122
				order[2] = 0
				fix.Group.__init__(self, 1120, 1121, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoPosAmt(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 707
			order[1] = 708
			order[2] = 1055
			order[3] = 0
			fix.Group.__init__(self, 753, 707, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(78)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 687
			order[56] = 690
			order[57] = 990
			order[58] = 1152
			order[59] = 683
			order[60] = 564
			order[61] = 565
			order[62] = 539
			order[63] = 654
			order[64] = 587
			order[65] = 588
			order[66] = 637
			order[67] = 675
			order[68] = 1073
			order[69] = 1074
			order[70] = 1075
			order[71] = 1379
			order[72] = 1381
			order[73] = 1383
			order[74] = 1384
			order[75] = 1418
			order[76] = 1342
			order[77] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

		class NoLegStipulations(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 688
				order[1] = 689
				order[2] = 0
				fix.Group.__init__(self, 683, 688, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

		class NoOfLegUnderlyings(fix.Group):
			def __init__(self):
				order = fix.IntArray(16)
				order[0] = 1330
				order[1] = 1331
				order[2] = 1332
				order[3] = 1333
				order[4] = 1344
				order[5] = 1337
				order[6] = 1338
				order[7] = 1339
				order[8] = 1345
				order[9] = 1405
				order[10] = 1340
				order[11] = 1391
				order[12] = 1343
				order[13] = 1341
				order[14] = 1392
				order[15] = 0
				fix.Group.__init__(self, 1342, 1330, order)

			class NoUnderlyingLegSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1335
					order[1] = 1336
					order[2] = 0
					fix.Group.__init__(self, 1334, 1335, order)

	class NoTrdRegTimestamps(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 769
			order[1] = 770
			order[2] = 771
			order[3] = 1033
			order[4] = 1034
			order[5] = 1035
			order[6] = 0
			fix.Group.__init__(self, 768, 769, order)

	class NoSides(fix.Group):
		def __init__(self):
			order = fix.IntArray(92)
			order[0] = 54
			order[1] = 1009
			order[2] = 1005
			order[3] = 1006
			order[4] = 1007
			order[5] = 83
			order[6] = 1008
			order[7] = 430
			order[8] = 1154
			order[9] = 1155
			order[10] = 453
			order[11] = 1
			order[12] = 660
			order[13] = 581
			order[14] = 81
			order[15] = 575
			order[16] = 576
			order[17] = 578
			order[18] = 579
			order[19] = 376
			order[20] = 377
			order[21] = 582
			order[22] = 336
			order[23] = 625
			order[24] = 943
			order[25] = 12
			order[26] = 13
			order[27] = 479
			order[28] = 497
			order[29] = 157
			order[30] = 230
			order[31] = 158
			order[32] = 159
			order[33] = 738
			order[34] = 920
			order[35] = 921
			order[36] = 922
			order[37] = 238
			order[38] = 237
			order[39] = 118
			order[40] = 119
			order[41] = 155
			order[42] = 156
			order[43] = 77
			order[44] = 58
			order[45] = 354
			order[46] = 355
			order[47] = 752
			order[48] = 518
			order[49] = 232
			order[50] = 136
			order[51] = 825
			order[52] = 826
			order[53] = 591
			order[54] = 70
			order[55] = 78
			order[56] = 1016
			order[57] = 1158
			order[58] = 1072
			order[59] = 1057
			order[60] = 1139
			order[61] = 1115
			order[62] = 37
			order[63] = 198
			order[64] = 11
			order[65] = 526
			order[66] = 66
			order[67] = 1080
			order[68] = 1081
			order[69] = 1431
			order[70] = 40
			order[71] = 44
			order[72] = 99
			order[73] = 18
			order[74] = 39
			order[75] = 151
			order[76] = 14
			order[77] = 59
			order[78] = 126
			order[79] = 528
			order[80] = 529
			order[81] = 1432
			order[82] = 821
			order[83] = 1093
			order[84] = 483
			order[85] = 586
			order[86] = 775
			order[87] = 1427
			order[88] = 1428
			order[89] = 1429
			order[90] = 1444
			order[91] = 0
			fix.Group.__init__(self, 552, 54, order)

		class NoPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 448
				order[1] = 447
				order[2] = 452
				order[3] = 2376
				order[4] = 802
				order[5] = 0
				fix.Group.__init__(self, 453, 448, order)

			class NoPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 523
					order[1] = 803
					order[2] = 0
					fix.Group.__init__(self, 802, 523, order)

		class NoClearingInstructions(fix.Group):
			def __init__(self):
				order = fix.IntArray(2)
				order[0] = 577
				order[1] = 0
				fix.Group.__init__(self, 576, 577, order)

		class NoContAmts(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 519
				order[1] = 520
				order[2] = 521
				order[3] = 0
				fix.Group.__init__(self, 518, 519, order)

		class NoStipulations(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 233
				order[1] = 234
				order[2] = 0
				fix.Group.__init__(self, 232, 233, order)

		class NoMiscFees(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 137
				order[1] = 138
				order[2] = 139
				order[3] = 891
				order[4] = 0
				fix.Group.__init__(self, 136, 137, order)

		class NoAllocs(fix.Group):
			def __init__(self):
				order = fix.IntArray(11)
				order[0] = 79
				order[1] = 661
				order[2] = 736
				order[3] = 467
				order[4] = 756
				order[5] = 80
				order[6] = 993
				order[7] = 1002
				order[8] = 989
				order[9] = 1136
				order[10] = 0
				fix.Group.__init__(self, 78, 79, order)

			class NoNested2PartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 757
					order[1] = 758
					order[2] = 759
					order[3] = 806
					order[4] = 0
					fix.Group.__init__(self, 756, 757, order)

				class NoNested2PartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 760
						order[1] = 807
						order[2] = 0
						fix.Group.__init__(self, 806, 760, order)

		class NoSideTrdRegTS(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1012
				order[1] = 1013
				order[2] = 1014
				order[3] = 0
				fix.Group.__init__(self, 1016, 1012, order)

		class NoSettlDetails(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1164
				order[1] = 781
				order[2] = 0
				fix.Group.__init__(self, 1158, 1164, order)

			class NoSettlPartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 782
					order[1] = 783
					order[2] = 784
					order[3] = 801
					order[4] = 0
					fix.Group.__init__(self, 781, 782, order)

				class NoSettlPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 785
						order[1] = 786
						order[2] = 0
						fix.Group.__init__(self, 801, 785, order)

	class NoTrdRepIndicators(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 1388
			order[1] = 1389
			order[2] = 0
			fix.Group.__init__(self, 1387, 1388, order)

class OrderMassStatusRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AF") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyingSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 458
			order[1] = 459
			order[2] = 0
			fix.Group.__init__(self, 457, 458, order)

	class NoUnderlyingStips(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 888
			order[1] = 889
			order[2] = 0
			fix.Group.__init__(self, 887, 888, order)

	class NoUndlyInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1059
			order[1] = 1060
			order[2] = 1061
			order[3] = 1062
			order[4] = 0
			fix.Group.__init__(self, 1058, 1059, order)

		class NoUndlyInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1063
				order[1] = 1064
				order[2] = 0
				fix.Group.__init__(self, 1062, 1063, order)

	class NoTargetPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1462
			order[1] = 1463
			order[2] = 1464
			order[3] = 0
			fix.Group.__init__(self, 1461, 1462, order)

class QuoteRequestReject(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AG") )

	class NoRootPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1117
			order[1] = 1118
			order[2] = 1119
			order[3] = 1120
			order[4] = 0
			fix.Group.__init__(self, 1116, 1117, order)

		class NoRootPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1121
				order[1] = 1122
				order[2] = 0
				fix.Group.__init__(self, 1120, 1121, order)

	class NoRelatedSym(fix.Group):
		def __init__(self):
			order = fix.IntArray(139)
			order[0] = 55
			order[1] = 65
			order[2] = 48
			order[3] = 22
			order[4] = 460
			order[5] = 1227
			order[6] = 1151
			order[7] = 461
			order[8] = 167
			order[9] = 762
			order[10] = 200
			order[11] = 541
			order[12] = 1079
			order[13] = 966
			order[14] = 1049
			order[15] = 965
			order[16] = 224
			order[17] = 225
			order[18] = 239
			order[19] = 226
			order[20] = 227
			order[21] = 228
			order[22] = 255
			order[23] = 543
			order[24] = 470
			order[25] = 471
			order[26] = 472
			order[27] = 240
			order[28] = 202
			order[29] = 947
			order[30] = 967
			order[31] = 968
			order[32] = 206
			order[33] = 231
			order[34] = 969
			order[35] = 1146
			order[36] = 996
			order[37] = 1147
			order[38] = 1191
			order[39] = 1192
			order[40] = 1193
			order[41] = 1194
			order[42] = 1195
			order[43] = 1196
			order[44] = 1197
			order[45] = 1198
			order[46] = 1199
			order[47] = 1200
			order[48] = 201
			order[49] = 1244
			order[50] = 1242
			order[51] = 997
			order[52] = 223
			order[53] = 207
			order[54] = 970
			order[55] = 971
			order[56] = 106
			order[57] = 348
			order[58] = 349
			order[59] = 107
			order[60] = 350
			order[61] = 351
			order[62] = 691
			order[63] = 667
			order[64] = 875
			order[65] = 876
			order[66] = 873
			order[67] = 874
			order[68] = 1435
			order[69] = 1439
			order[70] = 1449
			order[71] = 1450
			order[72] = 1451
			order[73] = 1452
			order[74] = 1457
			order[75] = 1458
			order[76] = 1478
			order[77] = 1479
			order[78] = 1480
			order[79] = 1481
			order[80] = 1482
			order[81] = 913
			order[82] = 914
			order[83] = 915
			order[84] = 918
			order[85] = 788
			order[86] = 916
			order[87] = 917
			order[88] = 919
			order[89] = 898
			order[90] = 711
			order[91] = 140
			order[92] = 303
			order[93] = 537
			order[94] = 336
			order[95] = 625
			order[96] = 229
			order[97] = 54
			order[98] = 854
			order[99] = 38
			order[100] = 152
			order[101] = 516
			order[102] = 468
			order[103] = 469
			order[104] = 63
			order[105] = 64
			order[106] = 193
			order[107] = 192
			order[108] = 15
			order[109] = 232
			order[110] = 1
			order[111] = 660
			order[112] = 581
			order[113] = 555
			order[114] = 735
			order[115] = 692
			order[116] = 40
			order[117] = 126
			order[118] = 60
			order[119] = 218
			order[120] = 22048
			order[121] = 220
			order[122] = 221
			order[123] = 222
			order[124] = 662
			order[125] = 663
			order[126] = 699
			order[127] = 761
			order[128] = 423
			order[129] = 44
			order[130] = 640
			order[131] = 235
			order[132] = 236
			order[133] = 701
			order[134] = 696
			order[135] = 697
			order[136] = 698
			order[137] = 453
			order[138] = 0
			fix.Group.__init__(self, 146, 55, order)

		class NoSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 455
				order[1] = 456
				order[2] = 0
				fix.Group.__init__(self, 454, 455, order)

		class NoEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 865
				order[1] = 866
				order[2] = 1145
				order[3] = 867
				order[4] = 868
				order[5] = 0
				fix.Group.__init__(self, 864, 865, order)

		class NoInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1019
				order[1] = 1050
				order[2] = 1051
				order[3] = 1052
				order[4] = 0
				fix.Group.__init__(self, 1018, 1019, order)

			class NoInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1053
					order[1] = 1054
					order[2] = 0
					fix.Group.__init__(self, 1052, 1053, order)

		class NoComplexEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(9)
				order[0] = 1484
				order[1] = 1485
				order[2] = 1486
				order[3] = 1487
				order[4] = 1488
				order[5] = 1489
				order[6] = 1490
				order[7] = 1491
				order[8] = 0
				fix.Group.__init__(self, 1483, 1484, order)

			class NoComplexEventDates(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1492
					order[1] = 1493
					order[2] = 1494
					order[3] = 0
					fix.Group.__init__(self, 1491, 1492, order)

				class NoComplexEventTimes(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1495
						order[1] = 1496
						order[2] = 0
						fix.Group.__init__(self, 1494, 1495, order)

		class NoUnderlyings(fix.Group):
			def __init__(self):
				order = fix.IntArray(70)
				order[0] = 311
				order[1] = 312
				order[2] = 309
				order[3] = 305
				order[4] = 462
				order[5] = 463
				order[6] = 310
				order[7] = 763
				order[8] = 313
				order[9] = 542
				order[10] = 1213
				order[11] = 241
				order[12] = 242
				order[13] = 243
				order[14] = 244
				order[15] = 245
				order[16] = 246
				order[17] = 256
				order[18] = 595
				order[19] = 592
				order[20] = 593
				order[21] = 594
				order[22] = 247
				order[23] = 316
				order[24] = 941
				order[25] = 317
				order[26] = 436
				order[27] = 998
				order[28] = 1423
				order[29] = 1424
				order[30] = 1425
				order[31] = 1000
				order[32] = 1419
				order[33] = 435
				order[34] = 308
				order[35] = 306
				order[36] = 362
				order[37] = 363
				order[38] = 307
				order[39] = 364
				order[40] = 365
				order[41] = 877
				order[42] = 878
				order[43] = 972
				order[44] = 318
				order[45] = 879
				order[46] = 975
				order[47] = 973
				order[48] = 974
				order[49] = 810
				order[50] = 882
				order[51] = 883
				order[52] = 884
				order[53] = 885
				order[54] = 886
				order[55] = 1044
				order[56] = 1045
				order[57] = 1046
				order[58] = 1038
				order[59] = 1039
				order[60] = 315
				order[61] = 1437
				order[62] = 1441
				order[63] = 1453
				order[64] = 1454
				order[65] = 1455
				order[66] = 1456
				order[67] = 1459
				order[68] = 1460
				order[69] = 0
				fix.Group.__init__(self, 711, 311, order)

			class NoUnderlyingSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 458
					order[1] = 459
					order[2] = 0
					fix.Group.__init__(self, 457, 458, order)

			class NoUnderlyingStips(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 888
					order[1] = 889
					order[2] = 0
					fix.Group.__init__(self, 887, 888, order)

			class NoUndlyInstrumentParties(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 1059
					order[1] = 1060
					order[2] = 1061
					order[3] = 1062
					order[4] = 0
					fix.Group.__init__(self, 1058, 1059, order)

				class NoUndlyInstrumentPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1063
						order[1] = 1064
						order[2] = 0
						fix.Group.__init__(self, 1062, 1063, order)

		class NoStipulations(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 233
				order[1] = 234
				order[2] = 0
				fix.Group.__init__(self, 232, 233, order)

		class NoLegs(fix.Group):
			def __init__(self):
				order = fix.IntArray(69)
				order[0] = 600
				order[1] = 601
				order[2] = 602
				order[3] = 603
				order[4] = 1788
				order[5] = 607
				order[6] = 608
				order[7] = 609
				order[8] = 764
				order[9] = 610
				order[10] = 611
				order[11] = 1212
				order[12] = 248
				order[13] = 249
				order[14] = 250
				order[15] = 251
				order[16] = 252
				order[17] = 253
				order[18] = 257
				order[19] = 599
				order[20] = 596
				order[21] = 597
				order[22] = 598
				order[23] = 254
				order[24] = 612
				order[25] = 942
				order[26] = 613
				order[27] = 614
				order[28] = 999
				order[29] = 1224
				order[30] = 1421
				order[31] = 1422
				order[32] = 1001
				order[33] = 1420
				order[34] = 615
				order[35] = 616
				order[36] = 617
				order[37] = 618
				order[38] = 619
				order[39] = 620
				order[40] = 621
				order[41] = 622
				order[42] = 623
				order[43] = 624
				order[44] = 556
				order[45] = 740
				order[46] = 739
				order[47] = 955
				order[48] = 956
				order[49] = 1358
				order[50] = 1017
				order[51] = 1436
				order[52] = 1440
				order[53] = 22041
				order[54] = 22049
				order[55] = 687
				order[56] = 685
				order[57] = 690
				order[58] = 587
				order[59] = 588
				order[60] = 683
				order[61] = 539
				order[62] = 676
				order[63] = 677
				order[64] = 678
				order[65] = 679
				order[66] = 680
				order[67] = 654
				order[68] = 0
				fix.Group.__init__(self, 555, 600, order)

			class NoLegSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 605
					order[1] = 606
					order[2] = 0
					fix.Group.__init__(self, 604, 605, order)

			class NoLegStipulations(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 688
					order[1] = 689
					order[2] = 0
					fix.Group.__init__(self, 683, 688, order)

			class NoNestedPartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 524
					order[1] = 525
					order[2] = 538
					order[3] = 804
					order[4] = 0
					fix.Group.__init__(self, 539, 524, order)

				class NoNestedPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 545
						order[1] = 805
						order[2] = 0
						fix.Group.__init__(self, 804, 545, order)

		class NoQuoteQualifiers(fix.Group):
			def __init__(self):
				order = fix.IntArray(2)
				order[0] = 695
				order[1] = 0
				fix.Group.__init__(self, 735, 695, order)

		class NoPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 448
				order[1] = 447
				order[2] = 452
				order[3] = 2376
				order[4] = 802
				order[5] = 0
				fix.Group.__init__(self, 453, 448, order)

			class NoPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 523
					order[1] = 803
					order[2] = 0
					fix.Group.__init__(self, 802, 523, order)

class RFQRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AH") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoRelatedSym(fix.Group):
		def __init__(self):
			order = fix.IntArray(89)
			order[0] = 55
			order[1] = 65
			order[2] = 48
			order[3] = 22
			order[4] = 460
			order[5] = 1227
			order[6] = 1151
			order[7] = 461
			order[8] = 167
			order[9] = 762
			order[10] = 200
			order[11] = 541
			order[12] = 1079
			order[13] = 966
			order[14] = 1049
			order[15] = 965
			order[16] = 224
			order[17] = 225
			order[18] = 239
			order[19] = 226
			order[20] = 227
			order[21] = 228
			order[22] = 255
			order[23] = 543
			order[24] = 470
			order[25] = 471
			order[26] = 472
			order[27] = 240
			order[28] = 202
			order[29] = 947
			order[30] = 967
			order[31] = 968
			order[32] = 206
			order[33] = 231
			order[34] = 969
			order[35] = 1146
			order[36] = 996
			order[37] = 1147
			order[38] = 1191
			order[39] = 1192
			order[40] = 1193
			order[41] = 1194
			order[42] = 1195
			order[43] = 1196
			order[44] = 1197
			order[45] = 1198
			order[46] = 1199
			order[47] = 1200
			order[48] = 201
			order[49] = 1244
			order[50] = 1242
			order[51] = 997
			order[52] = 223
			order[53] = 207
			order[54] = 970
			order[55] = 971
			order[56] = 106
			order[57] = 348
			order[58] = 349
			order[59] = 107
			order[60] = 350
			order[61] = 351
			order[62] = 691
			order[63] = 667
			order[64] = 875
			order[65] = 876
			order[66] = 873
			order[67] = 874
			order[68] = 1435
			order[69] = 1439
			order[70] = 1449
			order[71] = 1450
			order[72] = 1451
			order[73] = 1452
			order[74] = 1457
			order[75] = 1458
			order[76] = 1478
			order[77] = 1479
			order[78] = 1480
			order[79] = 1481
			order[80] = 1482
			order[81] = 711
			order[82] = 555
			order[83] = 140
			order[84] = 303
			order[85] = 537
			order[86] = 336
			order[87] = 625
			order[88] = 0
			fix.Group.__init__(self, 146, 55, order)

		class NoSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 455
				order[1] = 456
				order[2] = 0
				fix.Group.__init__(self, 454, 455, order)

		class NoEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 865
				order[1] = 866
				order[2] = 1145
				order[3] = 867
				order[4] = 868
				order[5] = 0
				fix.Group.__init__(self, 864, 865, order)

		class NoInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1019
				order[1] = 1050
				order[2] = 1051
				order[3] = 1052
				order[4] = 0
				fix.Group.__init__(self, 1018, 1019, order)

			class NoInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1053
					order[1] = 1054
					order[2] = 0
					fix.Group.__init__(self, 1052, 1053, order)

		class NoComplexEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(9)
				order[0] = 1484
				order[1] = 1485
				order[2] = 1486
				order[3] = 1487
				order[4] = 1488
				order[5] = 1489
				order[6] = 1490
				order[7] = 1491
				order[8] = 0
				fix.Group.__init__(self, 1483, 1484, order)

			class NoComplexEventDates(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1492
					order[1] = 1493
					order[2] = 1494
					order[3] = 0
					fix.Group.__init__(self, 1491, 1492, order)

				class NoComplexEventTimes(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1495
						order[1] = 1496
						order[2] = 0
						fix.Group.__init__(self, 1494, 1495, order)

		class NoUnderlyings(fix.Group):
			def __init__(self):
				order = fix.IntArray(70)
				order[0] = 311
				order[1] = 312
				order[2] = 309
				order[3] = 305
				order[4] = 462
				order[5] = 463
				order[6] = 310
				order[7] = 763
				order[8] = 313
				order[9] = 542
				order[10] = 1213
				order[11] = 241
				order[12] = 242
				order[13] = 243
				order[14] = 244
				order[15] = 245
				order[16] = 246
				order[17] = 256
				order[18] = 595
				order[19] = 592
				order[20] = 593
				order[21] = 594
				order[22] = 247
				order[23] = 316
				order[24] = 941
				order[25] = 317
				order[26] = 436
				order[27] = 998
				order[28] = 1423
				order[29] = 1424
				order[30] = 1425
				order[31] = 1000
				order[32] = 1419
				order[33] = 435
				order[34] = 308
				order[35] = 306
				order[36] = 362
				order[37] = 363
				order[38] = 307
				order[39] = 364
				order[40] = 365
				order[41] = 877
				order[42] = 878
				order[43] = 972
				order[44] = 318
				order[45] = 879
				order[46] = 975
				order[47] = 973
				order[48] = 974
				order[49] = 810
				order[50] = 882
				order[51] = 883
				order[52] = 884
				order[53] = 885
				order[54] = 886
				order[55] = 1044
				order[56] = 1045
				order[57] = 1046
				order[58] = 1038
				order[59] = 1039
				order[60] = 315
				order[61] = 1437
				order[62] = 1441
				order[63] = 1453
				order[64] = 1454
				order[65] = 1455
				order[66] = 1456
				order[67] = 1459
				order[68] = 1460
				order[69] = 0
				fix.Group.__init__(self, 711, 311, order)

			class NoUnderlyingSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 458
					order[1] = 459
					order[2] = 0
					fix.Group.__init__(self, 457, 458, order)

			class NoUnderlyingStips(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 888
					order[1] = 889
					order[2] = 0
					fix.Group.__init__(self, 887, 888, order)

			class NoUndlyInstrumentParties(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 1059
					order[1] = 1060
					order[2] = 1061
					order[3] = 1062
					order[4] = 0
					fix.Group.__init__(self, 1058, 1059, order)

				class NoUndlyInstrumentPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1063
						order[1] = 1064
						order[2] = 0
						fix.Group.__init__(self, 1062, 1063, order)

		class NoLegs(fix.Group):
			def __init__(self):
				order = fix.IntArray(56)
				order[0] = 600
				order[1] = 601
				order[2] = 602
				order[3] = 603
				order[4] = 1788
				order[5] = 607
				order[6] = 608
				order[7] = 609
				order[8] = 764
				order[9] = 610
				order[10] = 611
				order[11] = 1212
				order[12] = 248
				order[13] = 249
				order[14] = 250
				order[15] = 251
				order[16] = 252
				order[17] = 253
				order[18] = 257
				order[19] = 599
				order[20] = 596
				order[21] = 597
				order[22] = 598
				order[23] = 254
				order[24] = 612
				order[25] = 942
				order[26] = 613
				order[27] = 614
				order[28] = 999
				order[29] = 1224
				order[30] = 1421
				order[31] = 1422
				order[32] = 1001
				order[33] = 1420
				order[34] = 615
				order[35] = 616
				order[36] = 617
				order[37] = 618
				order[38] = 619
				order[39] = 620
				order[40] = 621
				order[41] = 622
				order[42] = 623
				order[43] = 624
				order[44] = 556
				order[45] = 740
				order[46] = 739
				order[47] = 955
				order[48] = 956
				order[49] = 1358
				order[50] = 1017
				order[51] = 1436
				order[52] = 1440
				order[53] = 22041
				order[54] = 22049
				order[55] = 0
				fix.Group.__init__(self, 555, 600, order)

			class NoLegSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 605
					order[1] = 606
					order[2] = 0
					fix.Group.__init__(self, 604, 605, order)

class QuoteStatusReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AI") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(63)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 687
			order[56] = 685
			order[57] = 690
			order[58] = 587
			order[59] = 588
			order[60] = 683
			order[61] = 539
			order[62] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

		class NoLegStipulations(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 688
				order[1] = 689
				order[2] = 0
				fix.Group.__init__(self, 683, 688, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

	class NoQuoteQualifiers(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 695
			order[1] = 0
			fix.Group.__init__(self, 735, 695, order)

	class NoTargetPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1462
			order[1] = 1463
			order[2] = 1464
			order[3] = 0
			fix.Group.__init__(self, 1461, 1462, order)

class QuoteResponse(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AJ") )

	class NoQuoteQualifiers(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 695
			order[1] = 0
			fix.Group.__init__(self, 735, 695, order)

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(74)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 687
			order[56] = 685
			order[57] = 690
			order[58] = 587
			order[59] = 588
			order[60] = 683
			order[61] = 539
			order[62] = 686
			order[63] = 681
			order[64] = 684
			order[65] = 676
			order[66] = 677
			order[67] = 678
			order[68] = 679
			order[69] = 680
			order[70] = 654
			order[71] = 1067
			order[72] = 1068
			order[73] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

		class NoLegStipulations(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 688
				order[1] = 689
				order[2] = 0
				fix.Group.__init__(self, 683, 688, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

class Confirmation(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AK") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoOrders(fix.Group):
		def __init__(self):
			order = fix.IntArray(10)
			order[0] = 11
			order[1] = 37
			order[2] = 198
			order[3] = 526
			order[4] = 66
			order[5] = 756
			order[6] = 38
			order[7] = 799
			order[8] = 800
			order[9] = 0
			fix.Group.__init__(self, 73, 11, order)

		class NoNested2PartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 757
				order[1] = 758
				order[2] = 759
				order[3] = 806
				order[4] = 0
				fix.Group.__init__(self, 756, 757, order)

			class NoNested2PartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 760
					order[1] = 807
					order[2] = 0
					fix.Group.__init__(self, 806, 760, order)

	class NoTrdRegTimestamps(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 769
			order[1] = 770
			order[2] = 771
			order[3] = 1033
			order[4] = 1034
			order[5] = 1035
			order[6] = 0
			fix.Group.__init__(self, 768, 769, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoInstrAttrib(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 871
			order[1] = 872
			order[2] = 0
			fix.Group.__init__(self, 870, 871, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoCapacities(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 528
			order[1] = 529
			order[2] = 863
			order[3] = 0
			fix.Group.__init__(self, 862, 528, order)

	class NoDlvyInst(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 165
			order[1] = 787
			order[2] = 781
			order[3] = 0
			fix.Group.__init__(self, 85, 165, order)

		class NoSettlPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 782
				order[1] = 783
				order[2] = 784
				order[3] = 801
				order[4] = 0
				fix.Group.__init__(self, 781, 782, order)

			class NoSettlPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 785
					order[1] = 786
					order[2] = 0
					fix.Group.__init__(self, 801, 785, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoMiscFees(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 137
			order[1] = 138
			order[2] = 139
			order[3] = 891
			order[4] = 0
			fix.Group.__init__(self, 136, 137, order)

class PositionMaintenanceRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AL") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoTradingSessions(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 336
			order[1] = 625
			order[2] = 0
			fix.Group.__init__(self, 386, 336, order)

	class NoPositions(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 703
			order[1] = 704
			order[2] = 705
			order[3] = 706
			order[4] = 976
			order[5] = 539
			order[6] = 0
			fix.Group.__init__(self, 702, 703, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

	class NoPosAmt(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 707
			order[1] = 708
			order[2] = 1055
			order[3] = 0
			fix.Group.__init__(self, 753, 707, order)

class PositionMaintenanceReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AM") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoTradingSessions(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 336
			order[1] = 625
			order[2] = 0
			fix.Group.__init__(self, 386, 336, order)

	class NoPositions(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 703
			order[1] = 704
			order[2] = 705
			order[3] = 706
			order[4] = 976
			order[5] = 539
			order[6] = 0
			fix.Group.__init__(self, 702, 703, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

	class NoPosAmt(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 707
			order[1] = 708
			order[2] = 1055
			order[3] = 0
			fix.Group.__init__(self, 753, 707, order)

class RequestForPositions(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AN") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoTradingSessions(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 336
			order[1] = 625
			order[2] = 0
			fix.Group.__init__(self, 386, 336, order)

class RequestForPositionsAck(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AO") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

class PositionReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AP") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(74)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 732
			order[70] = 733
			order[71] = 1037
			order[72] = 984
			order[73] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

		class NoUnderlyingAmounts(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 985
				order[1] = 986
				order[2] = 987
				order[3] = 988
				order[4] = 0
				fix.Group.__init__(self, 984, 985, order)

	class NoPositions(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 703
			order[1] = 704
			order[2] = 705
			order[3] = 706
			order[4] = 976
			order[5] = 539
			order[6] = 0
			fix.Group.__init__(self, 702, 703, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

	class NoPosAmt(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 707
			order[1] = 708
			order[2] = 1055
			order[3] = 0
			fix.Group.__init__(self, 753, 707, order)

class TradeCaptureReportRequestAck(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AQ") )

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

class TradeCaptureReportAck(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AR") )

	class NoRootPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1117
			order[1] = 1118
			order[2] = 1119
			order[3] = 1120
			order[4] = 0
			fix.Group.__init__(self, 1116, 1117, order)

		class NoRootPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1121
				order[1] = 1122
				order[2] = 0
				fix.Group.__init__(self, 1120, 1121, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoTrdRepIndicators(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 1388
			order[1] = 1389
			order[2] = 0
			fix.Group.__init__(self, 1387, 1388, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(78)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 687
			order[56] = 690
			order[57] = 990
			order[58] = 1152
			order[59] = 683
			order[60] = 564
			order[61] = 565
			order[62] = 539
			order[63] = 654
			order[64] = 587
			order[65] = 588
			order[66] = 637
			order[67] = 675
			order[68] = 1073
			order[69] = 1074
			order[70] = 1075
			order[71] = 1379
			order[72] = 1381
			order[73] = 1383
			order[74] = 1384
			order[75] = 1418
			order[76] = 1342
			order[77] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

		class NoLegStipulations(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 688
				order[1] = 689
				order[2] = 0
				fix.Group.__init__(self, 683, 688, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

		class NoOfLegUnderlyings(fix.Group):
			def __init__(self):
				order = fix.IntArray(16)
				order[0] = 1330
				order[1] = 1331
				order[2] = 1332
				order[3] = 1333
				order[4] = 1344
				order[5] = 1337
				order[6] = 1338
				order[7] = 1339
				order[8] = 1345
				order[9] = 1405
				order[10] = 1340
				order[11] = 1391
				order[12] = 1343
				order[13] = 1341
				order[14] = 1392
				order[15] = 0
				fix.Group.__init__(self, 1342, 1330, order)

			class NoUnderlyingLegSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1335
					order[1] = 1336
					order[2] = 0
					fix.Group.__init__(self, 1334, 1335, order)

	class NoTrdRegTimestamps(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 769
			order[1] = 770
			order[2] = 771
			order[3] = 1033
			order[4] = 1034
			order[5] = 1035
			order[6] = 0
			fix.Group.__init__(self, 768, 769, order)

	class NoPosAmt(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 707
			order[1] = 708
			order[2] = 1055
			order[3] = 0
			fix.Group.__init__(self, 753, 707, order)

	class NoSides(fix.Group):
		def __init__(self):
			order = fix.IntArray(87)
			order[0] = 54
			order[1] = 453
			order[2] = 1
			order[3] = 660
			order[4] = 581
			order[5] = 81
			order[6] = 575
			order[7] = 576
			order[8] = 578
			order[9] = 579
			order[10] = 376
			order[11] = 377
			order[12] = 582
			order[13] = 336
			order[14] = 625
			order[15] = 943
			order[16] = 430
			order[17] = 1154
			order[18] = 1155
			order[19] = 12
			order[20] = 13
			order[21] = 479
			order[22] = 497
			order[23] = 157
			order[24] = 230
			order[25] = 158
			order[26] = 159
			order[27] = 738
			order[28] = 920
			order[29] = 921
			order[30] = 922
			order[31] = 238
			order[32] = 237
			order[33] = 118
			order[34] = 119
			order[35] = 155
			order[36] = 156
			order[37] = 77
			order[38] = 752
			order[39] = 518
			order[40] = 232
			order[41] = 136
			order[42] = 825
			order[43] = 1158
			order[44] = 826
			order[45] = 591
			order[46] = 70
			order[47] = 78
			order[48] = 1072
			order[49] = 1057
			order[50] = 1009
			order[51] = 1005
			order[52] = 1006
			order[53] = 1007
			order[54] = 83
			order[55] = 1008
			order[56] = 1016
			order[57] = 1427
			order[58] = 1428
			order[59] = 1429
			order[60] = 1115
			order[61] = 37
			order[62] = 198
			order[63] = 11
			order[64] = 526
			order[65] = 66
			order[66] = 1080
			order[67] = 1081
			order[68] = 1431
			order[69] = 40
			order[70] = 44
			order[71] = 99
			order[72] = 18
			order[73] = 39
			order[74] = 151
			order[75] = 14
			order[76] = 59
			order[77] = 126
			order[78] = 528
			order[79] = 529
			order[80] = 1432
			order[81] = 821
			order[82] = 1093
			order[83] = 483
			order[84] = 586
			order[85] = 775
			order[86] = 0
			fix.Group.__init__(self, 552, 54, order)

		class NoPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 448
				order[1] = 447
				order[2] = 452
				order[3] = 2376
				order[4] = 802
				order[5] = 0
				fix.Group.__init__(self, 453, 448, order)

			class NoPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 523
					order[1] = 803
					order[2] = 0
					fix.Group.__init__(self, 802, 523, order)

		class NoClearingInstructions(fix.Group):
			def __init__(self):
				order = fix.IntArray(2)
				order[0] = 577
				order[1] = 0
				fix.Group.__init__(self, 576, 577, order)

		class NoContAmts(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 519
				order[1] = 520
				order[2] = 521
				order[3] = 0
				fix.Group.__init__(self, 518, 519, order)

		class NoStipulations(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 233
				order[1] = 234
				order[2] = 0
				fix.Group.__init__(self, 232, 233, order)

		class NoMiscFees(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 137
				order[1] = 138
				order[2] = 139
				order[3] = 891
				order[4] = 0
				fix.Group.__init__(self, 136, 137, order)

		class NoSettlDetails(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1164
				order[1] = 781
				order[2] = 0
				fix.Group.__init__(self, 1158, 1164, order)

			class NoSettlPartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 782
					order[1] = 783
					order[2] = 784
					order[3] = 801
					order[4] = 0
					fix.Group.__init__(self, 781, 782, order)

				class NoSettlPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 785
						order[1] = 786
						order[2] = 0
						fix.Group.__init__(self, 801, 785, order)

		class NoAllocs(fix.Group):
			def __init__(self):
				order = fix.IntArray(11)
				order[0] = 79
				order[1] = 661
				order[2] = 736
				order[3] = 467
				order[4] = 756
				order[5] = 80
				order[6] = 993
				order[7] = 1002
				order[8] = 989
				order[9] = 1136
				order[10] = 0
				fix.Group.__init__(self, 78, 79, order)

			class NoNested2PartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 757
					order[1] = 758
					order[2] = 759
					order[3] = 806
					order[4] = 0
					fix.Group.__init__(self, 756, 757, order)

				class NoNested2PartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 760
						order[1] = 807
						order[2] = 0
						fix.Group.__init__(self, 806, 760, order)

		class NoSideTrdRegTS(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1012
				order[1] = 1013
				order[2] = 1014
				order[3] = 0
				fix.Group.__init__(self, 1016, 1012, order)

class AllocationReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AS") )

	class NoOrders(fix.Group):
		def __init__(self):
			order = fix.IntArray(10)
			order[0] = 11
			order[1] = 37
			order[2] = 198
			order[3] = 526
			order[4] = 66
			order[5] = 756
			order[6] = 38
			order[7] = 799
			order[8] = 800
			order[9] = 0
			fix.Group.__init__(self, 73, 11, order)

		class NoNested2PartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 757
				order[1] = 758
				order[2] = 759
				order[3] = 806
				order[4] = 0
				fix.Group.__init__(self, 756, 757, order)

			class NoNested2PartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 760
					order[1] = 807
					order[2] = 0
					fix.Group.__init__(self, 806, 760, order)

	class NoExecs(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 32
			order[1] = 17
			order[2] = 527
			order[3] = 31
			order[4] = 669
			order[5] = 29
			order[6] = 1003
			order[7] = 1041
			order[8] = 0
			fix.Group.__init__(self, 124, 32, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoInstrAttrib(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 871
			order[1] = 872
			order[2] = 0
			fix.Group.__init__(self, 870, 871, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoPosAmt(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 707
			order[1] = 708
			order[2] = 1055
			order[3] = 0
			fix.Group.__init__(self, 753, 707, order)

	class NoAllocs(fix.Group):
		def __init__(self):
			order = fix.IntArray(41)
			order[0] = 79
			order[1] = 661
			order[2] = 573
			order[3] = 366
			order[4] = 80
			order[5] = 467
			order[6] = 81
			order[7] = 989
			order[8] = 1002
			order[9] = 993
			order[10] = 1047
			order[11] = 992
			order[12] = 539
			order[13] = 208
			order[14] = 209
			order[15] = 161
			order[16] = 360
			order[17] = 361
			order[18] = 12
			order[19] = 13
			order[20] = 479
			order[21] = 497
			order[22] = 153
			order[23] = 154
			order[24] = 119
			order[25] = 737
			order[26] = 120
			order[27] = 736
			order[28] = 155
			order[29] = 156
			order[30] = 742
			order[31] = 741
			order[32] = 136
			order[33] = 576
			order[34] = 635
			order[35] = 780
			order[36] = 172
			order[37] = 169
			order[38] = 170
			order[39] = 171
			order[40] = 0
			fix.Group.__init__(self, 78, 79, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

		class NoMiscFees(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 137
				order[1] = 138
				order[2] = 139
				order[3] = 891
				order[4] = 0
				fix.Group.__init__(self, 136, 137, order)

		class NoClearingInstructions(fix.Group):
			def __init__(self):
				order = fix.IntArray(2)
				order[0] = 577
				order[1] = 0
				fix.Group.__init__(self, 576, 577, order)

		class NoDlvyInst(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 165
				order[1] = 787
				order[2] = 781
				order[3] = 0
				fix.Group.__init__(self, 85, 165, order)

			class NoSettlPartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 782
					order[1] = 783
					order[2] = 784
					order[3] = 801
					order[4] = 0
					fix.Group.__init__(self, 781, 782, order)

				class NoSettlPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 785
						order[1] = 786
						order[2] = 0
						fix.Group.__init__(self, 801, 785, order)

	class NoRateSources(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1446
			order[1] = 1447
			order[2] = 1448
			order[3] = 0
			fix.Group.__init__(self, 1445, 1446, order)

class AllocationReportAck(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AT") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoAllocs(fix.Group):
		def __init__(self):
			order = fix.IntArray(15)
			order[0] = 79
			order[1] = 661
			order[2] = 366
			order[3] = 1047
			order[4] = 467
			order[5] = 776
			order[6] = 539
			order[7] = 161
			order[8] = 360
			order[9] = 361
			order[10] = 989
			order[11] = 993
			order[12] = 992
			order[13] = 80
			order[14] = 0
			fix.Group.__init__(self, 78, 79, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

class ConfirmationAck(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AU") )

class SettlementInstructionRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AV") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

class AssignmentReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AW") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoPositions(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 703
			order[1] = 704
			order[2] = 705
			order[3] = 706
			order[4] = 976
			order[5] = 539
			order[6] = 0
			fix.Group.__init__(self, 702, 703, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

	class NoPosAmt(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 707
			order[1] = 708
			order[2] = 1055
			order[3] = 0
			fix.Group.__init__(self, 753, 707, order)

class CollateralRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AX") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoExecs(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 17
			order[1] = 0
			fix.Group.__init__(self, 124, 17, order)

	class NoTrades(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 571
			order[1] = 818
			order[2] = 0
			fix.Group.__init__(self, 897, 571, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(71)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 944
			order[70] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoTrdRegTimestamps(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 769
			order[1] = 770
			order[2] = 771
			order[3] = 1033
			order[4] = 1034
			order[5] = 1035
			order[6] = 0
			fix.Group.__init__(self, 768, 769, order)

	class NoMiscFees(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 137
			order[1] = 138
			order[2] = 139
			order[3] = 891
			order[4] = 0
			fix.Group.__init__(self, 136, 137, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

class CollateralAssignment(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AY") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoExecs(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 17
			order[1] = 0
			fix.Group.__init__(self, 124, 17, order)

	class NoTrades(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 571
			order[1] = 818
			order[2] = 0
			fix.Group.__init__(self, 897, 571, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(71)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 944
			order[70] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoTrdRegTimestamps(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 769
			order[1] = 770
			order[2] = 771
			order[3] = 1033
			order[4] = 1034
			order[5] = 1035
			order[6] = 0
			fix.Group.__init__(self, 768, 769, order)

	class NoMiscFees(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 137
			order[1] = 138
			order[2] = 139
			order[3] = 891
			order[4] = 0
			fix.Group.__init__(self, 136, 137, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoDlvyInst(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 165
			order[1] = 787
			order[2] = 781
			order[3] = 0
			fix.Group.__init__(self, 85, 165, order)

		class NoSettlPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 782
				order[1] = 783
				order[2] = 784
				order[3] = 801
				order[4] = 0
				fix.Group.__init__(self, 781, 782, order)

			class NoSettlPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 785
					order[1] = 786
					order[2] = 0
					fix.Group.__init__(self, 801, 785, order)

class CollateralResponse(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("AZ") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoExecs(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 17
			order[1] = 0
			fix.Group.__init__(self, 124, 17, order)

	class NoTrades(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 571
			order[1] = 818
			order[2] = 0
			fix.Group.__init__(self, 897, 571, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(71)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 944
			order[70] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoTrdRegTimestamps(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 769
			order[1] = 770
			order[2] = 771
			order[3] = 1033
			order[4] = 1034
			order[5] = 1035
			order[6] = 0
			fix.Group.__init__(self, 768, 769, order)

	class NoMiscFees(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 137
			order[1] = 138
			order[2] = 139
			order[3] = 891
			order[4] = 0
			fix.Group.__init__(self, 136, 137, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

class CollateralReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BA") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoExecs(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 17
			order[1] = 0
			fix.Group.__init__(self, 124, 17, order)

	class NoTrades(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 571
			order[1] = 818
			order[2] = 0
			fix.Group.__init__(self, 897, 571, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoTrdRegTimestamps(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 769
			order[1] = 770
			order[2] = 771
			order[3] = 1033
			order[4] = 1034
			order[5] = 1035
			order[6] = 0
			fix.Group.__init__(self, 768, 769, order)

	class NoMiscFees(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 137
			order[1] = 138
			order[2] = 139
			order[3] = 891
			order[4] = 0
			fix.Group.__init__(self, 136, 137, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoDlvyInst(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 165
			order[1] = 787
			order[2] = 781
			order[3] = 0
			fix.Group.__init__(self, 85, 165, order)

		class NoSettlPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 782
				order[1] = 783
				order[2] = 784
				order[3] = 801
				order[4] = 0
				fix.Group.__init__(self, 781, 782, order)

			class NoSettlPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 785
					order[1] = 786
					order[2] = 0
					fix.Group.__init__(self, 801, 785, order)

class CollateralInquiry(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BB") )

	class NoCollInquiryQualifier(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 896
			order[1] = 0
			fix.Group.__init__(self, 938, 896, order)

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoExecs(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 17
			order[1] = 0
			fix.Group.__init__(self, 124, 17, order)

	class NoTrades(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 571
			order[1] = 818
			order[2] = 0
			fix.Group.__init__(self, 897, 571, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoTrdRegTimestamps(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 769
			order[1] = 770
			order[2] = 771
			order[3] = 1033
			order[4] = 1034
			order[5] = 1035
			order[6] = 0
			fix.Group.__init__(self, 768, 769, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoDlvyInst(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 165
			order[1] = 787
			order[2] = 781
			order[3] = 0
			fix.Group.__init__(self, 85, 165, order)

		class NoSettlPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 782
				order[1] = 783
				order[2] = 784
				order[3] = 801
				order[4] = 0
				fix.Group.__init__(self, 781, 782, order)

			class NoSettlPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 785
					order[1] = 786
					order[2] = 0
					fix.Group.__init__(self, 801, 785, order)

class NetworkCounterpartySystemStatusRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BC") )

	class NoCompIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 930
			order[1] = 931
			order[2] = 283
			order[3] = 284
			order[4] = 0
			fix.Group.__init__(self, 936, 930, order)

class NetworkCounterpartySystemStatusResponse(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BD") )

	class NoCompIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 930
			order[1] = 931
			order[2] = 283
			order[3] = 284
			order[4] = 928
			order[5] = 929
			order[6] = 0
			fix.Group.__init__(self, 936, 930, order)

class UserRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BE") )

class UserResponse(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BF") )

class CollateralInquiryAck(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BG") )

	class NoCollInquiryQualifier(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 896
			order[1] = 0
			fix.Group.__init__(self, 938, 896, order)

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoExecs(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 17
			order[1] = 0
			fix.Group.__init__(self, 124, 17, order)

	class NoTrades(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 571
			order[1] = 818
			order[2] = 0
			fix.Group.__init__(self, 897, 571, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

class ConfirmationRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BH") )

	class NoOrders(fix.Group):
		def __init__(self):
			order = fix.IntArray(10)
			order[0] = 11
			order[1] = 37
			order[2] = 198
			order[3] = 526
			order[4] = 66
			order[5] = 756
			order[6] = 38
			order[7] = 799
			order[8] = 800
			order[9] = 0
			fix.Group.__init__(self, 73, 11, order)

		class NoNested2PartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 757
				order[1] = 758
				order[2] = 759
				order[3] = 806
				order[4] = 0
				fix.Group.__init__(self, 756, 757, order)

			class NoNested2PartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 760
					order[1] = 807
					order[2] = 0
					fix.Group.__init__(self, 806, 760, order)

class ContraryIntentionReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BO") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoExpiration(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 982
			order[1] = 983
			order[2] = 0
			fix.Group.__init__(self, 981, 982, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

class SecurityDefinitionUpdateReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BP") )

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoInstrAttrib(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 871
			order[1] = 872
			order[2] = 0
			fix.Group.__init__(self, 870, 871, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoMarketSegments(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1301
			order[1] = 1300
			order[2] = 1201
			order[3] = 0
			fix.Group.__init__(self, 1310, 1301, order)

		class NoTickRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1206
				order[1] = 1207
				order[2] = 1208
				order[3] = 1209
				order[4] = 0
				fix.Group.__init__(self, 1205, 1206, order)

		class NoLotTypeRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1093
				order[1] = 1231
				order[2] = 0
				fix.Group.__init__(self, 1234, 1093, order)

		class NoTradingSessionRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 336
				order[1] = 625
				order[2] = 0
				fix.Group.__init__(self, 1309, 336, order)

			class NoOrdTypeRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 40
					order[1] = 0
					fix.Group.__init__(self, 1237, 40, order)

			class NoTimeInForceRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 59
					order[1] = 0
					fix.Group.__init__(self, 1239, 59, order)

			class NoExecInstRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 1308
					order[1] = 0
					fix.Group.__init__(self, 1232, 1308, order)

			class NoMatchRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1142
					order[1] = 574
					order[2] = 0
					fix.Group.__init__(self, 1235, 1142, order)

			class NoMDFeedTypes(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1022
					order[1] = 264
					order[2] = 1021
					order[3] = 0
					fix.Group.__init__(self, 1141, 1022, order)

		class NoNestedInstrAttrib(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1210
				order[1] = 1211
				order[2] = 0
				fix.Group.__init__(self, 1312, 1210, order)

		class NoStrikeRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(7)
				order[0] = 1223
				order[1] = 1202
				order[2] = 1203
				order[3] = 1204
				order[4] = 1304
				order[5] = 1236
				order[6] = 0
				fix.Group.__init__(self, 1201, 1223, order)

			class NoMaturityRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(7)
					order[0] = 1222
					order[1] = 1303
					order[2] = 1302
					order[3] = 1241
					order[4] = 1226
					order[5] = 1229
					order[6] = 0
					fix.Group.__init__(self, 1236, 1222, order)

class SecurityListUpdateReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BK") )

	class NoRelatedSym(fix.Group):
		def __init__(self):
			order = fix.IntArray(118)
			order[0] = 1324
			order[1] = 55
			order[2] = 65
			order[3] = 48
			order[4] = 22
			order[5] = 460
			order[6] = 1227
			order[7] = 1151
			order[8] = 461
			order[9] = 167
			order[10] = 762
			order[11] = 200
			order[12] = 541
			order[13] = 1079
			order[14] = 966
			order[15] = 1049
			order[16] = 965
			order[17] = 224
			order[18] = 225
			order[19] = 239
			order[20] = 226
			order[21] = 227
			order[22] = 228
			order[23] = 255
			order[24] = 543
			order[25] = 470
			order[26] = 471
			order[27] = 472
			order[28] = 240
			order[29] = 202
			order[30] = 947
			order[31] = 967
			order[32] = 968
			order[33] = 206
			order[34] = 231
			order[35] = 969
			order[36] = 1146
			order[37] = 996
			order[38] = 1147
			order[39] = 1191
			order[40] = 1192
			order[41] = 1193
			order[42] = 1194
			order[43] = 1195
			order[44] = 1196
			order[45] = 1197
			order[46] = 1198
			order[47] = 1199
			order[48] = 1200
			order[49] = 201
			order[50] = 1244
			order[51] = 1242
			order[52] = 997
			order[53] = 223
			order[54] = 207
			order[55] = 970
			order[56] = 971
			order[57] = 106
			order[58] = 348
			order[59] = 349
			order[60] = 107
			order[61] = 350
			order[62] = 351
			order[63] = 691
			order[64] = 667
			order[65] = 875
			order[66] = 876
			order[67] = 873
			order[68] = 874
			order[69] = 1435
			order[70] = 1439
			order[71] = 1449
			order[72] = 1450
			order[73] = 1451
			order[74] = 1452
			order[75] = 1457
			order[76] = 1458
			order[77] = 1478
			order[78] = 1479
			order[79] = 1480
			order[80] = 1481
			order[81] = 1482
			order[82] = 668
			order[83] = 869
			order[84] = 913
			order[85] = 914
			order[86] = 915
			order[87] = 918
			order[88] = 788
			order[89] = 916
			order[90] = 917
			order[91] = 919
			order[92] = 898
			order[93] = 1201
			order[94] = 711
			order[95] = 15
			order[96] = 232
			order[97] = 555
			order[98] = 218
			order[99] = 22048
			order[100] = 220
			order[101] = 221
			order[102] = 222
			order[103] = 662
			order[104] = 663
			order[105] = 699
			order[106] = 761
			order[107] = 235
			order[108] = 236
			order[109] = 701
			order[110] = 696
			order[111] = 697
			order[112] = 698
			order[113] = 58
			order[114] = 354
			order[115] = 355
			order[116] = 1504
			order[117] = 0
			fix.Group.__init__(self, 146, 1324, order)

		class NoSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 455
				order[1] = 456
				order[2] = 0
				fix.Group.__init__(self, 454, 455, order)

		class NoEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 865
				order[1] = 866
				order[2] = 1145
				order[3] = 867
				order[4] = 868
				order[5] = 0
				fix.Group.__init__(self, 864, 865, order)

		class NoInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1019
				order[1] = 1050
				order[2] = 1051
				order[3] = 1052
				order[4] = 0
				fix.Group.__init__(self, 1018, 1019, order)

			class NoInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1053
					order[1] = 1054
					order[2] = 0
					fix.Group.__init__(self, 1052, 1053, order)

		class NoComplexEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(9)
				order[0] = 1484
				order[1] = 1485
				order[2] = 1486
				order[3] = 1487
				order[4] = 1488
				order[5] = 1489
				order[6] = 1490
				order[7] = 1491
				order[8] = 0
				fix.Group.__init__(self, 1483, 1484, order)

			class NoComplexEventDates(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1492
					order[1] = 1493
					order[2] = 1494
					order[3] = 0
					fix.Group.__init__(self, 1491, 1492, order)

				class NoComplexEventTimes(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1495
						order[1] = 1496
						order[2] = 0
						fix.Group.__init__(self, 1494, 1495, order)

		class NoInstrAttrib(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 871
				order[1] = 872
				order[2] = 0
				fix.Group.__init__(self, 870, 871, order)

		class NoTickRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1206
				order[1] = 1207
				order[2] = 1208
				order[3] = 1209
				order[4] = 0
				fix.Group.__init__(self, 1205, 1206, order)

		class NoLotTypeRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1093
				order[1] = 1231
				order[2] = 0
				fix.Group.__init__(self, 1234, 1093, order)

		class NoTradingSessionRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 336
				order[1] = 625
				order[2] = 0
				fix.Group.__init__(self, 1309, 336, order)

			class NoOrdTypeRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 40
					order[1] = 0
					fix.Group.__init__(self, 1237, 40, order)

			class NoTimeInForceRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 59
					order[1] = 0
					fix.Group.__init__(self, 1239, 59, order)

			class NoExecInstRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 1308
					order[1] = 0
					fix.Group.__init__(self, 1232, 1308, order)

			class NoMatchRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1142
					order[1] = 574
					order[2] = 0
					fix.Group.__init__(self, 1235, 1142, order)

			class NoMDFeedTypes(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1022
					order[1] = 264
					order[2] = 1021
					order[3] = 0
					fix.Group.__init__(self, 1141, 1022, order)

		class NoNestedInstrAttrib(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1210
				order[1] = 1211
				order[2] = 0
				fix.Group.__init__(self, 1312, 1210, order)

		class NoStrikeRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(7)
				order[0] = 1223
				order[1] = 1202
				order[2] = 1203
				order[3] = 1204
				order[4] = 1304
				order[5] = 1236
				order[6] = 0
				fix.Group.__init__(self, 1201, 1223, order)

			class NoMaturityRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(7)
					order[0] = 1222
					order[1] = 1303
					order[2] = 1302
					order[3] = 1241
					order[4] = 1226
					order[5] = 1229
					order[6] = 0
					fix.Group.__init__(self, 1236, 1222, order)

		class NoUnderlyings(fix.Group):
			def __init__(self):
				order = fix.IntArray(70)
				order[0] = 311
				order[1] = 312
				order[2] = 309
				order[3] = 305
				order[4] = 462
				order[5] = 463
				order[6] = 310
				order[7] = 763
				order[8] = 313
				order[9] = 542
				order[10] = 1213
				order[11] = 241
				order[12] = 242
				order[13] = 243
				order[14] = 244
				order[15] = 245
				order[16] = 246
				order[17] = 256
				order[18] = 595
				order[19] = 592
				order[20] = 593
				order[21] = 594
				order[22] = 247
				order[23] = 316
				order[24] = 941
				order[25] = 317
				order[26] = 436
				order[27] = 998
				order[28] = 1423
				order[29] = 1424
				order[30] = 1425
				order[31] = 1000
				order[32] = 1419
				order[33] = 435
				order[34] = 308
				order[35] = 306
				order[36] = 362
				order[37] = 363
				order[38] = 307
				order[39] = 364
				order[40] = 365
				order[41] = 877
				order[42] = 878
				order[43] = 972
				order[44] = 318
				order[45] = 879
				order[46] = 975
				order[47] = 973
				order[48] = 974
				order[49] = 810
				order[50] = 882
				order[51] = 883
				order[52] = 884
				order[53] = 885
				order[54] = 886
				order[55] = 1044
				order[56] = 1045
				order[57] = 1046
				order[58] = 1038
				order[59] = 1039
				order[60] = 315
				order[61] = 1437
				order[62] = 1441
				order[63] = 1453
				order[64] = 1454
				order[65] = 1455
				order[66] = 1456
				order[67] = 1459
				order[68] = 1460
				order[69] = 0
				fix.Group.__init__(self, 711, 311, order)

			class NoUnderlyingSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 458
					order[1] = 459
					order[2] = 0
					fix.Group.__init__(self, 457, 458, order)

			class NoUnderlyingStips(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 888
					order[1] = 889
					order[2] = 0
					fix.Group.__init__(self, 887, 888, order)

			class NoUndlyInstrumentParties(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 1059
					order[1] = 1060
					order[2] = 1061
					order[3] = 1062
					order[4] = 0
					fix.Group.__init__(self, 1058, 1059, order)

				class NoUndlyInstrumentPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1063
						order[1] = 1064
						order[2] = 0
						fix.Group.__init__(self, 1062, 1063, order)

		class NoStipulations(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 233
				order[1] = 234
				order[2] = 0
				fix.Group.__init__(self, 232, 233, order)

		class NoLegs(fix.Group):
			def __init__(self):
				order = fix.IntArray(64)
				order[0] = 600
				order[1] = 601
				order[2] = 602
				order[3] = 603
				order[4] = 1788
				order[5] = 607
				order[6] = 608
				order[7] = 609
				order[8] = 764
				order[9] = 610
				order[10] = 611
				order[11] = 1212
				order[12] = 248
				order[13] = 249
				order[14] = 250
				order[15] = 251
				order[16] = 252
				order[17] = 253
				order[18] = 257
				order[19] = 599
				order[20] = 596
				order[21] = 597
				order[22] = 598
				order[23] = 254
				order[24] = 612
				order[25] = 942
				order[26] = 613
				order[27] = 614
				order[28] = 999
				order[29] = 1224
				order[30] = 1421
				order[31] = 1422
				order[32] = 1001
				order[33] = 1420
				order[34] = 615
				order[35] = 616
				order[36] = 617
				order[37] = 618
				order[38] = 619
				order[39] = 620
				order[40] = 621
				order[41] = 622
				order[42] = 623
				order[43] = 624
				order[44] = 556
				order[45] = 740
				order[46] = 739
				order[47] = 955
				order[48] = 956
				order[49] = 1358
				order[50] = 1017
				order[51] = 1436
				order[52] = 1440
				order[53] = 22041
				order[54] = 22049
				order[55] = 690
				order[56] = 587
				order[57] = 683
				order[58] = 676
				order[59] = 677
				order[60] = 678
				order[61] = 679
				order[62] = 680
				order[63] = 0
				fix.Group.__init__(self, 555, 600, order)

			class NoLegSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 605
					order[1] = 606
					order[2] = 0
					fix.Group.__init__(self, 604, 605, order)

			class NoLegStipulations(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 688
					order[1] = 689
					order[2] = 0
					fix.Group.__init__(self, 683, 688, order)

class AdjustedPositionReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BL") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoPositions(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 703
			order[1] = 704
			order[2] = 705
			order[3] = 706
			order[4] = 976
			order[5] = 539
			order[6] = 0
			fix.Group.__init__(self, 702, 703, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

	class NoRelatedSym(fix.Group):
		def __init__(self):
			order = fix.IntArray(82)
			order[0] = 55
			order[1] = 65
			order[2] = 48
			order[3] = 22
			order[4] = 460
			order[5] = 1227
			order[6] = 1151
			order[7] = 461
			order[8] = 167
			order[9] = 762
			order[10] = 200
			order[11] = 541
			order[12] = 1079
			order[13] = 966
			order[14] = 1049
			order[15] = 965
			order[16] = 224
			order[17] = 225
			order[18] = 239
			order[19] = 226
			order[20] = 227
			order[21] = 228
			order[22] = 255
			order[23] = 543
			order[24] = 470
			order[25] = 471
			order[26] = 472
			order[27] = 240
			order[28] = 202
			order[29] = 947
			order[30] = 967
			order[31] = 968
			order[32] = 206
			order[33] = 231
			order[34] = 969
			order[35] = 1146
			order[36] = 996
			order[37] = 1147
			order[38] = 1191
			order[39] = 1192
			order[40] = 1193
			order[41] = 1194
			order[42] = 1195
			order[43] = 1196
			order[44] = 1197
			order[45] = 1198
			order[46] = 1199
			order[47] = 1200
			order[48] = 201
			order[49] = 1244
			order[50] = 1242
			order[51] = 997
			order[52] = 223
			order[53] = 207
			order[54] = 970
			order[55] = 971
			order[56] = 106
			order[57] = 348
			order[58] = 349
			order[59] = 107
			order[60] = 350
			order[61] = 351
			order[62] = 691
			order[63] = 667
			order[64] = 875
			order[65] = 876
			order[66] = 873
			order[67] = 874
			order[68] = 1435
			order[69] = 1439
			order[70] = 1449
			order[71] = 1450
			order[72] = 1451
			order[73] = 1452
			order[74] = 1457
			order[75] = 1458
			order[76] = 1478
			order[77] = 1479
			order[78] = 1480
			order[79] = 1481
			order[80] = 1482
			order[81] = 0
			fix.Group.__init__(self, 146, 55, order)

		class NoSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 455
				order[1] = 456
				order[2] = 0
				fix.Group.__init__(self, 454, 455, order)

		class NoEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 865
				order[1] = 866
				order[2] = 1145
				order[3] = 867
				order[4] = 868
				order[5] = 0
				fix.Group.__init__(self, 864, 865, order)

		class NoInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1019
				order[1] = 1050
				order[2] = 1051
				order[3] = 1052
				order[4] = 0
				fix.Group.__init__(self, 1018, 1019, order)

			class NoInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1053
					order[1] = 1054
					order[2] = 0
					fix.Group.__init__(self, 1052, 1053, order)

		class NoComplexEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(9)
				order[0] = 1484
				order[1] = 1485
				order[2] = 1486
				order[3] = 1487
				order[4] = 1488
				order[5] = 1489
				order[6] = 1490
				order[7] = 1491
				order[8] = 0
				fix.Group.__init__(self, 1483, 1484, order)

			class NoComplexEventDates(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1492
					order[1] = 1493
					order[2] = 1494
					order[3] = 0
					fix.Group.__init__(self, 1491, 1492, order)

				class NoComplexEventTimes(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1495
						order[1] = 1496
						order[2] = 0
						fix.Group.__init__(self, 1494, 1495, order)

class AllocationInstructionAlert(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BM") )

	class NoOrders(fix.Group):
		def __init__(self):
			order = fix.IntArray(10)
			order[0] = 11
			order[1] = 37
			order[2] = 198
			order[3] = 526
			order[4] = 66
			order[5] = 756
			order[6] = 38
			order[7] = 799
			order[8] = 800
			order[9] = 0
			fix.Group.__init__(self, 73, 11, order)

		class NoNested2PartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 757
				order[1] = 758
				order[2] = 759
				order[3] = 806
				order[4] = 0
				fix.Group.__init__(self, 756, 757, order)

			class NoNested2PartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 760
					order[1] = 807
					order[2] = 0
					fix.Group.__init__(self, 806, 760, order)

	class NoExecs(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 32
			order[1] = 17
			order[2] = 527
			order[3] = 31
			order[4] = 669
			order[5] = 29
			order[6] = 1003
			order[7] = 1041
			order[8] = 0
			fix.Group.__init__(self, 124, 32, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoInstrAttrib(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 871
			order[1] = 872
			order[2] = 0
			fix.Group.__init__(self, 870, 871, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoStipulations(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 233
			order[1] = 234
			order[2] = 0
			fix.Group.__init__(self, 232, 233, order)

	class NoPosAmt(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 707
			order[1] = 708
			order[2] = 1055
			order[3] = 0
			fix.Group.__init__(self, 753, 707, order)

	class NoAllocs(fix.Group):
		def __init__(self):
			order = fix.IntArray(41)
			order[0] = 79
			order[1] = 661
			order[2] = 573
			order[3] = 366
			order[4] = 80
			order[5] = 467
			order[6] = 81
			order[7] = 989
			order[8] = 1002
			order[9] = 993
			order[10] = 1047
			order[11] = 992
			order[12] = 539
			order[13] = 208
			order[14] = 209
			order[15] = 161
			order[16] = 360
			order[17] = 361
			order[18] = 12
			order[19] = 13
			order[20] = 479
			order[21] = 497
			order[22] = 153
			order[23] = 154
			order[24] = 119
			order[25] = 737
			order[26] = 120
			order[27] = 736
			order[28] = 155
			order[29] = 156
			order[30] = 742
			order[31] = 741
			order[32] = 136
			order[33] = 576
			order[34] = 635
			order[35] = 780
			order[36] = 172
			order[37] = 169
			order[38] = 170
			order[39] = 171
			order[40] = 0
			fix.Group.__init__(self, 78, 79, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

		class NoMiscFees(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 137
				order[1] = 138
				order[2] = 139
				order[3] = 891
				order[4] = 0
				fix.Group.__init__(self, 136, 137, order)

		class NoClearingInstructions(fix.Group):
			def __init__(self):
				order = fix.IntArray(2)
				order[0] = 577
				order[1] = 0
				fix.Group.__init__(self, 576, 577, order)

		class NoDlvyInst(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 165
				order[1] = 787
				order[2] = 781
				order[3] = 0
				fix.Group.__init__(self, 85, 165, order)

			class NoSettlPartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 782
					order[1] = 783
					order[2] = 784
					order[3] = 801
					order[4] = 0
					fix.Group.__init__(self, 781, 782, order)

				class NoSettlPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 785
						order[1] = 786
						order[2] = 0
						fix.Group.__init__(self, 801, 785, order)

class ExecutionAcknowledgement(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BN") )

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyings(fix.Group):
		def __init__(self):
			order = fix.IntArray(70)
			order[0] = 311
			order[1] = 312
			order[2] = 309
			order[3] = 305
			order[4] = 462
			order[5] = 463
			order[6] = 310
			order[7] = 763
			order[8] = 313
			order[9] = 542
			order[10] = 1213
			order[11] = 241
			order[12] = 242
			order[13] = 243
			order[14] = 244
			order[15] = 245
			order[16] = 246
			order[17] = 256
			order[18] = 595
			order[19] = 592
			order[20] = 593
			order[21] = 594
			order[22] = 247
			order[23] = 316
			order[24] = 941
			order[25] = 317
			order[26] = 436
			order[27] = 998
			order[28] = 1423
			order[29] = 1424
			order[30] = 1425
			order[31] = 1000
			order[32] = 1419
			order[33] = 435
			order[34] = 308
			order[35] = 306
			order[36] = 362
			order[37] = 363
			order[38] = 307
			order[39] = 364
			order[40] = 365
			order[41] = 877
			order[42] = 878
			order[43] = 972
			order[44] = 318
			order[45] = 879
			order[46] = 975
			order[47] = 973
			order[48] = 974
			order[49] = 810
			order[50] = 882
			order[51] = 883
			order[52] = 884
			order[53] = 885
			order[54] = 886
			order[55] = 1044
			order[56] = 1045
			order[57] = 1046
			order[58] = 1038
			order[59] = 1039
			order[60] = 315
			order[61] = 1437
			order[62] = 1441
			order[63] = 1453
			order[64] = 1454
			order[65] = 1455
			order[66] = 1456
			order[67] = 1459
			order[68] = 1460
			order[69] = 0
			fix.Group.__init__(self, 711, 311, order)

		class NoUnderlyingSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 458
				order[1] = 459
				order[2] = 0
				fix.Group.__init__(self, 457, 458, order)

		class NoUnderlyingStips(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 888
				order[1] = 889
				order[2] = 0
				fix.Group.__init__(self, 887, 888, order)

		class NoUndlyInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1059
				order[1] = 1060
				order[2] = 1061
				order[3] = 1062
				order[4] = 0
				fix.Group.__init__(self, 1058, 1059, order)

			class NoUndlyInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1063
					order[1] = 1064
					order[2] = 0
					fix.Group.__init__(self, 1062, 1063, order)

	class NoLegs(fix.Group):
		def __init__(self):
			order = fix.IntArray(56)
			order[0] = 600
			order[1] = 601
			order[2] = 602
			order[3] = 603
			order[4] = 1788
			order[5] = 607
			order[6] = 608
			order[7] = 609
			order[8] = 764
			order[9] = 610
			order[10] = 611
			order[11] = 1212
			order[12] = 248
			order[13] = 249
			order[14] = 250
			order[15] = 251
			order[16] = 252
			order[17] = 253
			order[18] = 257
			order[19] = 599
			order[20] = 596
			order[21] = 597
			order[22] = 598
			order[23] = 254
			order[24] = 612
			order[25] = 942
			order[26] = 613
			order[27] = 614
			order[28] = 999
			order[29] = 1224
			order[30] = 1421
			order[31] = 1422
			order[32] = 1001
			order[33] = 1420
			order[34] = 615
			order[35] = 616
			order[36] = 617
			order[37] = 618
			order[38] = 619
			order[39] = 620
			order[40] = 621
			order[41] = 622
			order[42] = 623
			order[43] = 624
			order[44] = 556
			order[45] = 740
			order[46] = 739
			order[47] = 955
			order[48] = 956
			order[49] = 1358
			order[50] = 1017
			order[51] = 1436
			order[52] = 1440
			order[53] = 22041
			order[54] = 22049
			order[55] = 0
			fix.Group.__init__(self, 555, 600, order)

		class NoLegSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 605
				order[1] = 606
				order[2] = 0
				fix.Group.__init__(self, 604, 605, order)

class TradingSessionList(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BJ") )

	class NoTradingSessions(fix.Group):
		def __init__(self):
			order = fix.IntArray(23)
			order[0] = 336
			order[1] = 625
			order[2] = 207
			order[3] = 1301
			order[4] = 1300
			order[5] = 1326
			order[6] = 338
			order[7] = 339
			order[8] = 325
			order[9] = 340
			order[10] = 567
			order[11] = 341
			order[12] = 342
			order[13] = 343
			order[14] = 344
			order[15] = 345
			order[16] = 387
			order[17] = 58
			order[18] = 354
			order[19] = 355
			order[20] = 60
			order[21] = 1327
			order[22] = 0
			fix.Group.__init__(self, 386, 336, order)

		class NoOrdTypeRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(2)
				order[0] = 40
				order[1] = 0
				fix.Group.__init__(self, 1237, 40, order)

		class NoTimeInForceRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(2)
				order[0] = 59
				order[1] = 0
				fix.Group.__init__(self, 1239, 59, order)

		class NoExecInstRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(2)
				order[0] = 1308
				order[1] = 0
				fix.Group.__init__(self, 1232, 1308, order)

		class NoMatchRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1142
				order[1] = 574
				order[2] = 0
				fix.Group.__init__(self, 1235, 1142, order)

		class NoMDFeedTypes(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1022
				order[1] = 264
				order[2] = 1021
				order[3] = 0
				fix.Group.__init__(self, 1141, 1022, order)

class TradingSessionListRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BI") )

class SettlementObligationReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BQ") )

	class NoSettlOblig(fix.Group):
		def __init__(self):
			order = fix.IntArray(97)
			order[0] = 430
			order[1] = 1161
			order[2] = 1162
			order[3] = 1163
			order[4] = 1157
			order[5] = 119
			order[6] = 15
			order[7] = 120
			order[8] = 155
			order[9] = 64
			order[10] = 55
			order[11] = 65
			order[12] = 48
			order[13] = 22
			order[14] = 460
			order[15] = 1227
			order[16] = 1151
			order[17] = 461
			order[18] = 167
			order[19] = 762
			order[20] = 200
			order[21] = 541
			order[22] = 1079
			order[23] = 966
			order[24] = 1049
			order[25] = 965
			order[26] = 224
			order[27] = 225
			order[28] = 239
			order[29] = 226
			order[30] = 227
			order[31] = 228
			order[32] = 255
			order[33] = 543
			order[34] = 470
			order[35] = 471
			order[36] = 472
			order[37] = 240
			order[38] = 202
			order[39] = 947
			order[40] = 967
			order[41] = 968
			order[42] = 206
			order[43] = 231
			order[44] = 969
			order[45] = 1146
			order[46] = 996
			order[47] = 1147
			order[48] = 1191
			order[49] = 1192
			order[50] = 1193
			order[51] = 1194
			order[52] = 1195
			order[53] = 1196
			order[54] = 1197
			order[55] = 1198
			order[56] = 1199
			order[57] = 1200
			order[58] = 201
			order[59] = 1244
			order[60] = 1242
			order[61] = 997
			order[62] = 223
			order[63] = 207
			order[64] = 970
			order[65] = 971
			order[66] = 106
			order[67] = 348
			order[68] = 349
			order[69] = 107
			order[70] = 350
			order[71] = 351
			order[72] = 691
			order[73] = 667
			order[74] = 875
			order[75] = 876
			order[76] = 873
			order[77] = 874
			order[78] = 1435
			order[79] = 1439
			order[80] = 1449
			order[81] = 1450
			order[82] = 1451
			order[83] = 1452
			order[84] = 1457
			order[85] = 1458
			order[86] = 1478
			order[87] = 1479
			order[88] = 1480
			order[89] = 1481
			order[90] = 1482
			order[91] = 453
			order[92] = 168
			order[93] = 126
			order[94] = 779
			order[95] = 1158
			order[96] = 0
			fix.Group.__init__(self, 1165, 430, order)

		class NoSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 455
				order[1] = 456
				order[2] = 0
				fix.Group.__init__(self, 454, 455, order)

		class NoEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 865
				order[1] = 866
				order[2] = 1145
				order[3] = 867
				order[4] = 868
				order[5] = 0
				fix.Group.__init__(self, 864, 865, order)

		class NoInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1019
				order[1] = 1050
				order[2] = 1051
				order[3] = 1052
				order[4] = 0
				fix.Group.__init__(self, 1018, 1019, order)

			class NoInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1053
					order[1] = 1054
					order[2] = 0
					fix.Group.__init__(self, 1052, 1053, order)

		class NoComplexEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(9)
				order[0] = 1484
				order[1] = 1485
				order[2] = 1486
				order[3] = 1487
				order[4] = 1488
				order[5] = 1489
				order[6] = 1490
				order[7] = 1491
				order[8] = 0
				fix.Group.__init__(self, 1483, 1484, order)

			class NoComplexEventDates(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1492
					order[1] = 1493
					order[2] = 1494
					order[3] = 0
					fix.Group.__init__(self, 1491, 1492, order)

				class NoComplexEventTimes(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1495
						order[1] = 1496
						order[2] = 0
						fix.Group.__init__(self, 1494, 1495, order)

		class NoPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 448
				order[1] = 447
				order[2] = 452
				order[3] = 2376
				order[4] = 802
				order[5] = 0
				fix.Group.__init__(self, 453, 448, order)

			class NoPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 523
					order[1] = 803
					order[2] = 0
					fix.Group.__init__(self, 802, 523, order)

		class NoSettlDetails(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1164
				order[1] = 781
				order[2] = 0
				fix.Group.__init__(self, 1158, 1164, order)

			class NoSettlPartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 782
					order[1] = 783
					order[2] = 784
					order[3] = 801
					order[4] = 0
					fix.Group.__init__(self, 781, 782, order)

				class NoSettlPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 785
						order[1] = 786
						order[2] = 0
						fix.Group.__init__(self, 801, 785, order)

class DerivativeSecurityListUpdateReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BR") )

	class NoUnderlyingSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 458
			order[1] = 459
			order[2] = 0
			fix.Group.__init__(self, 457, 458, order)

	class NoUnderlyingStips(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 888
			order[1] = 889
			order[2] = 0
			fix.Group.__init__(self, 887, 888, order)

	class NoUndlyInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1059
			order[1] = 1060
			order[2] = 1061
			order[3] = 1062
			order[4] = 0
			fix.Group.__init__(self, 1058, 1059, order)

		class NoUndlyInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1063
				order[1] = 1064
				order[2] = 0
				fix.Group.__init__(self, 1062, 1063, order)

	class NoDerivativeSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 1219
			order[1] = 1220
			order[2] = 0
			fix.Group.__init__(self, 1218, 1219, order)

	class NoDerivativeEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 1287
			order[1] = 1288
			order[2] = 1289
			order[3] = 1290
			order[4] = 1291
			order[5] = 0
			fix.Group.__init__(self, 1286, 1287, order)

	class NoDerivativeInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1293
			order[1] = 1294
			order[2] = 1295
			order[3] = 1296
			order[4] = 0
			fix.Group.__init__(self, 1292, 1293, order)

		class NoDerivativeInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1297
				order[1] = 1298
				order[2] = 0
				fix.Group.__init__(self, 1296, 1297, order)

	class NoDerivativeInstrAttrib(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 1313
			order[1] = 1314
			order[2] = 0
			fix.Group.__init__(self, 1311, 1313, order)

	class NoMarketSegments(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1301
			order[1] = 1300
			order[2] = 1201
			order[3] = 0
			fix.Group.__init__(self, 1310, 1301, order)

		class NoTickRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1206
				order[1] = 1207
				order[2] = 1208
				order[3] = 1209
				order[4] = 0
				fix.Group.__init__(self, 1205, 1206, order)

		class NoLotTypeRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1093
				order[1] = 1231
				order[2] = 0
				fix.Group.__init__(self, 1234, 1093, order)

		class NoTradingSessionRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 336
				order[1] = 625
				order[2] = 0
				fix.Group.__init__(self, 1309, 336, order)

			class NoOrdTypeRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 40
					order[1] = 0
					fix.Group.__init__(self, 1237, 40, order)

			class NoTimeInForceRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 59
					order[1] = 0
					fix.Group.__init__(self, 1239, 59, order)

			class NoExecInstRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 1308
					order[1] = 0
					fix.Group.__init__(self, 1232, 1308, order)

			class NoMatchRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1142
					order[1] = 574
					order[2] = 0
					fix.Group.__init__(self, 1235, 1142, order)

			class NoMDFeedTypes(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1022
					order[1] = 264
					order[2] = 1021
					order[3] = 0
					fix.Group.__init__(self, 1141, 1022, order)

		class NoNestedInstrAttrib(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1210
				order[1] = 1211
				order[2] = 0
				fix.Group.__init__(self, 1312, 1210, order)

		class NoStrikeRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(7)
				order[0] = 1223
				order[1] = 1202
				order[2] = 1203
				order[3] = 1204
				order[4] = 1304
				order[5] = 1236
				order[6] = 0
				fix.Group.__init__(self, 1201, 1223, order)

			class NoMaturityRules(fix.Group):
				def __init__(self):
					order = fix.IntArray(7)
					order[0] = 1222
					order[1] = 1303
					order[2] = 1302
					order[3] = 1241
					order[4] = 1226
					order[5] = 1229
					order[6] = 0
					fix.Group.__init__(self, 1236, 1222, order)

	class NoRelatedSym(fix.Group):
		def __init__(self):
			order = fix.IntArray(96)
			order[0] = 1324
			order[1] = 292
			order[2] = 55
			order[3] = 65
			order[4] = 48
			order[5] = 22
			order[6] = 460
			order[7] = 1227
			order[8] = 1151
			order[9] = 461
			order[10] = 167
			order[11] = 762
			order[12] = 200
			order[13] = 541
			order[14] = 1079
			order[15] = 966
			order[16] = 1049
			order[17] = 965
			order[18] = 224
			order[19] = 225
			order[20] = 239
			order[21] = 226
			order[22] = 227
			order[23] = 228
			order[24] = 255
			order[25] = 543
			order[26] = 470
			order[27] = 471
			order[28] = 472
			order[29] = 240
			order[30] = 202
			order[31] = 947
			order[32] = 967
			order[33] = 968
			order[34] = 206
			order[35] = 231
			order[36] = 969
			order[37] = 1146
			order[38] = 996
			order[39] = 1147
			order[40] = 1191
			order[41] = 1192
			order[42] = 1193
			order[43] = 1194
			order[44] = 1195
			order[45] = 1196
			order[46] = 1197
			order[47] = 1198
			order[48] = 1199
			order[49] = 1200
			order[50] = 201
			order[51] = 1244
			order[52] = 1242
			order[53] = 997
			order[54] = 223
			order[55] = 207
			order[56] = 970
			order[57] = 971
			order[58] = 106
			order[59] = 348
			order[60] = 349
			order[61] = 107
			order[62] = 350
			order[63] = 351
			order[64] = 691
			order[65] = 667
			order[66] = 875
			order[67] = 876
			order[68] = 873
			order[69] = 874
			order[70] = 1435
			order[71] = 1439
			order[72] = 1449
			order[73] = 1450
			order[74] = 1451
			order[75] = 1452
			order[76] = 1457
			order[77] = 1458
			order[78] = 1478
			order[79] = 1479
			order[80] = 1480
			order[81] = 1481
			order[82] = 1482
			order[83] = 668
			order[84] = 869
			order[85] = 1305
			order[86] = 1221
			order[87] = 1230
			order[88] = 1240
			order[89] = 15
			order[90] = 555
			order[91] = 58
			order[92] = 354
			order[93] = 355
			order[94] = 1504
			order[95] = 0
			fix.Group.__init__(self, 146, 1324, order)

		class NoSecurityAltID(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 455
				order[1] = 456
				order[2] = 0
				fix.Group.__init__(self, 454, 455, order)

		class NoEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 865
				order[1] = 866
				order[2] = 1145
				order[3] = 867
				order[4] = 868
				order[5] = 0
				fix.Group.__init__(self, 864, 865, order)

		class NoInstrumentParties(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1019
				order[1] = 1050
				order[2] = 1051
				order[3] = 1052
				order[4] = 0
				fix.Group.__init__(self, 1018, 1019, order)

			class NoInstrumentPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1053
					order[1] = 1054
					order[2] = 0
					fix.Group.__init__(self, 1052, 1053, order)

		class NoComplexEvents(fix.Group):
			def __init__(self):
				order = fix.IntArray(9)
				order[0] = 1484
				order[1] = 1485
				order[2] = 1486
				order[3] = 1487
				order[4] = 1488
				order[5] = 1489
				order[6] = 1490
				order[7] = 1491
				order[8] = 0
				fix.Group.__init__(self, 1483, 1484, order)

			class NoComplexEventDates(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1492
					order[1] = 1493
					order[2] = 1494
					order[3] = 0
					fix.Group.__init__(self, 1491, 1492, order)

				class NoComplexEventTimes(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1495
						order[1] = 1496
						order[2] = 0
						fix.Group.__init__(self, 1494, 1495, order)

		class NoInstrAttrib(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 871
				order[1] = 872
				order[2] = 0
				fix.Group.__init__(self, 870, 871, order)

		class NoLegs(fix.Group):
			def __init__(self):
				order = fix.IntArray(56)
				order[0] = 600
				order[1] = 601
				order[2] = 602
				order[3] = 603
				order[4] = 1788
				order[5] = 607
				order[6] = 608
				order[7] = 609
				order[8] = 764
				order[9] = 610
				order[10] = 611
				order[11] = 1212
				order[12] = 248
				order[13] = 249
				order[14] = 250
				order[15] = 251
				order[16] = 252
				order[17] = 253
				order[18] = 257
				order[19] = 599
				order[20] = 596
				order[21] = 597
				order[22] = 598
				order[23] = 254
				order[24] = 612
				order[25] = 942
				order[26] = 613
				order[27] = 614
				order[28] = 999
				order[29] = 1224
				order[30] = 1421
				order[31] = 1422
				order[32] = 1001
				order[33] = 1420
				order[34] = 615
				order[35] = 616
				order[36] = 617
				order[37] = 618
				order[38] = 619
				order[39] = 620
				order[40] = 621
				order[41] = 622
				order[42] = 623
				order[43] = 624
				order[44] = 556
				order[45] = 740
				order[46] = 739
				order[47] = 955
				order[48] = 956
				order[49] = 1358
				order[50] = 1017
				order[51] = 1436
				order[52] = 1440
				order[53] = 22041
				order[54] = 22049
				order[55] = 0
				fix.Group.__init__(self, 555, 600, order)

			class NoLegSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 605
					order[1] = 606
					order[2] = 0
					fix.Group.__init__(self, 604, 605, order)

class TradingSessionListUpdateReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BS") )

	class NoTradingSessions(fix.Group):
		def __init__(self):
			order = fix.IntArray(23)
			order[0] = 336
			order[1] = 625
			order[2] = 207
			order[3] = 1301
			order[4] = 1300
			order[5] = 1326
			order[6] = 338
			order[7] = 339
			order[8] = 325
			order[9] = 340
			order[10] = 567
			order[11] = 341
			order[12] = 342
			order[13] = 343
			order[14] = 344
			order[15] = 345
			order[16] = 387
			order[17] = 58
			order[18] = 354
			order[19] = 355
			order[20] = 60
			order[21] = 1327
			order[22] = 0
			fix.Group.__init__(self, 386, 336, order)

		class NoOrdTypeRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(2)
				order[0] = 40
				order[1] = 0
				fix.Group.__init__(self, 1237, 40, order)

		class NoTimeInForceRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(2)
				order[0] = 59
				order[1] = 0
				fix.Group.__init__(self, 1239, 59, order)

		class NoExecInstRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(2)
				order[0] = 1308
				order[1] = 0
				fix.Group.__init__(self, 1232, 1308, order)

		class NoMatchRules(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1142
				order[1] = 574
				order[2] = 0
				fix.Group.__init__(self, 1235, 1142, order)

		class NoMDFeedTypes(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1022
				order[1] = 264
				order[2] = 1021
				order[3] = 0
				fix.Group.__init__(self, 1141, 1022, order)

class MarketDefinitionRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BT") )

class MarketDefinition(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BU") )

	class NoTickRules(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1206
			order[1] = 1207
			order[2] = 1208
			order[3] = 1209
			order[4] = 0
			fix.Group.__init__(self, 1205, 1206, order)

	class NoLotTypeRules(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 1093
			order[1] = 1231
			order[2] = 0
			fix.Group.__init__(self, 1234, 1093, order)

	class NoOrdTypeRules(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 40
			order[1] = 0
			fix.Group.__init__(self, 1237, 40, order)

	class NoTimeInForceRules(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 59
			order[1] = 0
			fix.Group.__init__(self, 1239, 59, order)

	class NoExecInstRules(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 1308
			order[1] = 0
			fix.Group.__init__(self, 1232, 1308, order)

class MarketDefinitionUpdateReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BV") )

	class NoTickRules(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1206
			order[1] = 1207
			order[2] = 1208
			order[3] = 1209
			order[4] = 0
			fix.Group.__init__(self, 1205, 1206, order)

	class NoLotTypeRules(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 1093
			order[1] = 1231
			order[2] = 0
			fix.Group.__init__(self, 1234, 1093, order)

	class NoOrdTypeRules(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 40
			order[1] = 0
			fix.Group.__init__(self, 1237, 40, order)

	class NoTimeInForceRules(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 59
			order[1] = 0
			fix.Group.__init__(self, 1239, 59, order)

	class NoExecInstRules(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 1308
			order[1] = 0
			fix.Group.__init__(self, 1232, 1308, order)

class ApplicationMessageRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BW") )

	class NoApplIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 1355
			order[1] = 1182
			order[2] = 1183
			order[3] = 539
			order[4] = 1433
			order[5] = 0
			fix.Group.__init__(self, 1351, 1355, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

class ApplicationMessageRequestAck(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BX") )

	class NoApplIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(8)
			order[0] = 1355
			order[1] = 1182
			order[2] = 1183
			order[3] = 1357
			order[4] = 1354
			order[5] = 539
			order[6] = 1433
			order[7] = 0
			fix.Group.__init__(self, 1351, 1355, order)

		class NoNestedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 524
				order[1] = 525
				order[2] = 538
				order[3] = 804
				order[4] = 0
				fix.Group.__init__(self, 539, 524, order)

			class NoNestedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 545
					order[1] = 805
					order[2] = 0
					fix.Group.__init__(self, 804, 545, order)

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

class ApplicationMessageReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BY") )

	class NoApplIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1355
			order[1] = 1399
			order[2] = 1357
			order[3] = 0
			fix.Group.__init__(self, 1351, 1355, order)

class OrderMassActionReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("BZ") )

	class NoAffectedOrders(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 41
			order[1] = 535
			order[2] = 536
			order[3] = 0
			fix.Group.__init__(self, 534, 41, order)

	class NoNotAffectedOrders(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 1372
			order[1] = 1371
			order[2] = 0
			fix.Group.__init__(self, 1370, 1372, order)

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyingSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 458
			order[1] = 459
			order[2] = 0
			fix.Group.__init__(self, 457, 458, order)

	class NoUnderlyingStips(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 888
			order[1] = 889
			order[2] = 0
			fix.Group.__init__(self, 887, 888, order)

	class NoUndlyInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1059
			order[1] = 1060
			order[2] = 1061
			order[3] = 1062
			order[4] = 0
			fix.Group.__init__(self, 1058, 1059, order)

		class NoUndlyInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1063
				order[1] = 1064
				order[2] = 0
				fix.Group.__init__(self, 1062, 1063, order)

	class NoTargetPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1462
			order[1] = 1463
			order[2] = 1464
			order[3] = 0
			fix.Group.__init__(self, 1461, 1462, order)

class OrderMassActionRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("CA") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 455
			order[1] = 456
			order[2] = 0
			fix.Group.__init__(self, 454, 455, order)

	class NoEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 865
			order[1] = 866
			order[2] = 1145
			order[3] = 867
			order[4] = 868
			order[5] = 0
			fix.Group.__init__(self, 864, 865, order)

	class NoInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1019
			order[1] = 1050
			order[2] = 1051
			order[3] = 1052
			order[4] = 0
			fix.Group.__init__(self, 1018, 1019, order)

		class NoInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1053
				order[1] = 1054
				order[2] = 0
				fix.Group.__init__(self, 1052, 1053, order)

	class NoComplexEvents(fix.Group):
		def __init__(self):
			order = fix.IntArray(9)
			order[0] = 1484
			order[1] = 1485
			order[2] = 1486
			order[3] = 1487
			order[4] = 1488
			order[5] = 1489
			order[6] = 1490
			order[7] = 1491
			order[8] = 0
			fix.Group.__init__(self, 1483, 1484, order)

		class NoComplexEventDates(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1492
				order[1] = 1493
				order[2] = 1494
				order[3] = 0
				fix.Group.__init__(self, 1491, 1492, order)

			class NoComplexEventTimes(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1495
					order[1] = 1496
					order[2] = 0
					fix.Group.__init__(self, 1494, 1495, order)

	class NoUnderlyingSecurityAltID(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 458
			order[1] = 459
			order[2] = 0
			fix.Group.__init__(self, 457, 458, order)

	class NoUnderlyingStips(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 888
			order[1] = 889
			order[2] = 0
			fix.Group.__init__(self, 887, 888, order)

	class NoUndlyInstrumentParties(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 1059
			order[1] = 1060
			order[2] = 1061
			order[3] = 1062
			order[4] = 0
			fix.Group.__init__(self, 1058, 1059, order)

		class NoUndlyInstrumentPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 1063
				order[1] = 1064
				order[2] = 0
				fix.Group.__init__(self, 1062, 1063, order)

	class NoTargetPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(4)
			order[0] = 1462
			order[1] = 1463
			order[2] = 1464
			order[3] = 0
			fix.Group.__init__(self, 1461, 1462, order)

class UserNotification(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("CB") )

class StreamAssignmentRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("CC") )

	class NoAsgnReqs(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 453
			order[1] = 146
			order[2] = 0
			fix.Group.__init__(self, 1499, 453, order)

		class NoPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 448
				order[1] = 447
				order[2] = 452
				order[3] = 2376
				order[4] = 802
				order[5] = 0
				fix.Group.__init__(self, 453, 448, order)

			class NoPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 523
					order[1] = 803
					order[2] = 0
					fix.Group.__init__(self, 802, 523, order)

		class NoRelatedSym(fix.Group):
			def __init__(self):
				order = fix.IntArray(85)
				order[0] = 55
				order[1] = 65
				order[2] = 48
				order[3] = 22
				order[4] = 460
				order[5] = 1227
				order[6] = 1151
				order[7] = 461
				order[8] = 167
				order[9] = 762
				order[10] = 200
				order[11] = 541
				order[12] = 1079
				order[13] = 966
				order[14] = 1049
				order[15] = 965
				order[16] = 224
				order[17] = 225
				order[18] = 239
				order[19] = 226
				order[20] = 227
				order[21] = 228
				order[22] = 255
				order[23] = 543
				order[24] = 470
				order[25] = 471
				order[26] = 472
				order[27] = 240
				order[28] = 202
				order[29] = 947
				order[30] = 967
				order[31] = 968
				order[32] = 206
				order[33] = 231
				order[34] = 969
				order[35] = 1146
				order[36] = 996
				order[37] = 1147
				order[38] = 1191
				order[39] = 1192
				order[40] = 1193
				order[41] = 1194
				order[42] = 1195
				order[43] = 1196
				order[44] = 1197
				order[45] = 1198
				order[46] = 1199
				order[47] = 1200
				order[48] = 201
				order[49] = 1244
				order[50] = 1242
				order[51] = 997
				order[52] = 223
				order[53] = 207
				order[54] = 970
				order[55] = 971
				order[56] = 106
				order[57] = 348
				order[58] = 349
				order[59] = 107
				order[60] = 350
				order[61] = 351
				order[62] = 691
				order[63] = 667
				order[64] = 875
				order[65] = 876
				order[66] = 873
				order[67] = 874
				order[68] = 1435
				order[69] = 1439
				order[70] = 1449
				order[71] = 1450
				order[72] = 1451
				order[73] = 1452
				order[74] = 1457
				order[75] = 1458
				order[76] = 1478
				order[77] = 1479
				order[78] = 1480
				order[79] = 1481
				order[80] = 1482
				order[81] = 63
				order[82] = 271
				order[83] = 1500
				order[84] = 0
				fix.Group.__init__(self, 146, 55, order)

			class NoSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 455
					order[1] = 456
					order[2] = 0
					fix.Group.__init__(self, 454, 455, order)

			class NoEvents(fix.Group):
				def __init__(self):
					order = fix.IntArray(6)
					order[0] = 865
					order[1] = 866
					order[2] = 1145
					order[3] = 867
					order[4] = 868
					order[5] = 0
					fix.Group.__init__(self, 864, 865, order)

			class NoInstrumentParties(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 1019
					order[1] = 1050
					order[2] = 1051
					order[3] = 1052
					order[4] = 0
					fix.Group.__init__(self, 1018, 1019, order)

				class NoInstrumentPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1053
						order[1] = 1054
						order[2] = 0
						fix.Group.__init__(self, 1052, 1053, order)

			class NoComplexEvents(fix.Group):
				def __init__(self):
					order = fix.IntArray(9)
					order[0] = 1484
					order[1] = 1485
					order[2] = 1486
					order[3] = 1487
					order[4] = 1488
					order[5] = 1489
					order[6] = 1490
					order[7] = 1491
					order[8] = 0
					fix.Group.__init__(self, 1483, 1484, order)

				class NoComplexEventDates(fix.Group):
					def __init__(self):
						order = fix.IntArray(4)
						order[0] = 1492
						order[1] = 1493
						order[2] = 1494
						order[3] = 0
						fix.Group.__init__(self, 1491, 1492, order)

					class NoComplexEventTimes(fix.Group):
						def __init__(self):
							order = fix.IntArray(3)
							order[0] = 1495
							order[1] = 1496
							order[2] = 0
							fix.Group.__init__(self, 1494, 1495, order)

class StreamAssignmentReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("CD") )

	class NoAsgnReqs(fix.Group):
		def __init__(self):
			order = fix.IntArray(3)
			order[0] = 453
			order[1] = 146
			order[2] = 0
			fix.Group.__init__(self, 1499, 453, order)

		class NoPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(6)
				order[0] = 448
				order[1] = 447
				order[2] = 452
				order[3] = 2376
				order[4] = 802
				order[5] = 0
				fix.Group.__init__(self, 453, 448, order)

			class NoPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 523
					order[1] = 803
					order[2] = 0
					fix.Group.__init__(self, 802, 523, order)

		class NoRelatedSym(fix.Group):
			def __init__(self):
				order = fix.IntArray(89)
				order[0] = 55
				order[1] = 65
				order[2] = 48
				order[3] = 22
				order[4] = 460
				order[5] = 1227
				order[6] = 1151
				order[7] = 461
				order[8] = 167
				order[9] = 762
				order[10] = 200
				order[11] = 541
				order[12] = 1079
				order[13] = 966
				order[14] = 1049
				order[15] = 965
				order[16] = 224
				order[17] = 225
				order[18] = 239
				order[19] = 226
				order[20] = 227
				order[21] = 228
				order[22] = 255
				order[23] = 543
				order[24] = 470
				order[25] = 471
				order[26] = 472
				order[27] = 240
				order[28] = 202
				order[29] = 947
				order[30] = 967
				order[31] = 968
				order[32] = 206
				order[33] = 231
				order[34] = 969
				order[35] = 1146
				order[36] = 996
				order[37] = 1147
				order[38] = 1191
				order[39] = 1192
				order[40] = 1193
				order[41] = 1194
				order[42] = 1195
				order[43] = 1196
				order[44] = 1197
				order[45] = 1198
				order[46] = 1199
				order[47] = 1200
				order[48] = 201
				order[49] = 1244
				order[50] = 1242
				order[51] = 997
				order[52] = 223
				order[53] = 207
				order[54] = 970
				order[55] = 971
				order[56] = 106
				order[57] = 348
				order[58] = 349
				order[59] = 107
				order[60] = 350
				order[61] = 351
				order[62] = 691
				order[63] = 667
				order[64] = 875
				order[65] = 876
				order[66] = 873
				order[67] = 874
				order[68] = 1435
				order[69] = 1439
				order[70] = 1449
				order[71] = 1450
				order[72] = 1451
				order[73] = 1452
				order[74] = 1457
				order[75] = 1458
				order[76] = 1478
				order[77] = 1479
				order[78] = 1480
				order[79] = 1481
				order[80] = 1482
				order[81] = 63
				order[82] = 1617
				order[83] = 1500
				order[84] = 1502
				order[85] = 58
				order[86] = 354
				order[87] = 355
				order[88] = 0
				fix.Group.__init__(self, 146, 55, order)

			class NoSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 455
					order[1] = 456
					order[2] = 0
					fix.Group.__init__(self, 454, 455, order)

			class NoEvents(fix.Group):
				def __init__(self):
					order = fix.IntArray(6)
					order[0] = 865
					order[1] = 866
					order[2] = 1145
					order[3] = 867
					order[4] = 868
					order[5] = 0
					fix.Group.__init__(self, 864, 865, order)

			class NoInstrumentParties(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 1019
					order[1] = 1050
					order[2] = 1051
					order[3] = 1052
					order[4] = 0
					fix.Group.__init__(self, 1018, 1019, order)

				class NoInstrumentPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1053
						order[1] = 1054
						order[2] = 0
						fix.Group.__init__(self, 1052, 1053, order)

			class NoComplexEvents(fix.Group):
				def __init__(self):
					order = fix.IntArray(9)
					order[0] = 1484
					order[1] = 1485
					order[2] = 1486
					order[3] = 1487
					order[4] = 1488
					order[5] = 1489
					order[6] = 1490
					order[7] = 1491
					order[8] = 0
					fix.Group.__init__(self, 1483, 1484, order)

				class NoComplexEventDates(fix.Group):
					def __init__(self):
						order = fix.IntArray(4)
						order[0] = 1492
						order[1] = 1493
						order[2] = 1494
						order[3] = 0
						fix.Group.__init__(self, 1491, 1492, order)

					class NoComplexEventTimes(fix.Group):
						def __init__(self):
							order = fix.IntArray(3)
							order[0] = 1495
							order[1] = 1496
							order[2] = 0
							fix.Group.__init__(self, 1494, 1495, order)

class StreamAssignmentReportACK(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("CE") )

class QuoteAcknowledgement(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("CW") )

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

class PartyDetailsListRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("CF") )

	class NoPartyListResponseTypes(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 1507
			order[1] = 0
			fix.Group.__init__(self, 1506, 1507, order)

	class NoPartyIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(6)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 2376
			order[4] = 802
			order[5] = 0
			fix.Group.__init__(self, 453, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

	class NoRequestedPartyRoles(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 1509
			order[1] = 0
			fix.Group.__init__(self, 1508, 1509, order)

	class NoPartyRelationships(fix.Group):
		def __init__(self):
			order = fix.IntArray(2)
			order[0] = 1515
			order[1] = 0
			fix.Group.__init__(self, 1514, 1515, order)

class PartyDetailsListReport(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("CG") )

	class NoPartyList(fix.Group):
		def __init__(self):
			order = fix.IntArray(5)
			order[0] = 448
			order[1] = 447
			order[2] = 452
			order[3] = 1562
			order[4] = 0
			fix.Group.__init__(self, 1513, 448, order)

		class NoPartySubIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(3)
				order[0] = 523
				order[1] = 803
				order[2] = 0
				fix.Group.__init__(self, 802, 523, order)

		class NoPartyAltIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(4)
				order[0] = 1517
				order[1] = 1518
				order[2] = 1519
				order[3] = 0
				fix.Group.__init__(self, 1516, 1517, order)

			class NoPartyAltSubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1520
					order[1] = 1521
					order[2] = 0
					fix.Group.__init__(self, 1519, 1520, order)

		class NoContextPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1523
				order[1] = 1524
				order[2] = 1525
				order[3] = 1526
				order[4] = 0
				fix.Group.__init__(self, 1522, 1523, order)

			class NoContextPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1527
					order[1] = 1528
					order[2] = 0
					fix.Group.__init__(self, 1526, 1527, order)

		class NoRiskLimits(fix.Group):
			def __init__(self):
				order = fix.IntArray(7)
				order[0] = 1530
				order[1] = 1531
				order[2] = 1532
				order[3] = 1533
				order[4] = 1534
				order[5] = 1559
				order[6] = 0
				fix.Group.__init__(self, 1529, 1530, order)

			class NoRiskInstruments(fix.Group):
				def __init__(self):
					order = fix.IntArray(26)
					order[0] = 1535
					order[1] = 1536
					order[2] = 1537
					order[3] = 1538
					order[4] = 1539
					order[5] = 1540
					order[6] = 1543
					order[7] = 1544
					order[8] = 1545
					order[9] = 1546
					order[10] = 1547
					order[11] = 1548
					order[12] = 1549
					order[13] = 1550
					order[14] = 1551
					order[15] = 1552
					order[16] = 1553
					order[17] = 1554
					order[18] = 1555
					order[19] = 1616
					order[20] = 1556
					order[21] = 1620
					order[22] = 1621
					order[23] = 1557
					order[24] = 1558
					order[25] = 0
					fix.Group.__init__(self, 1534, 1535, order)

				class NoRiskSecurityAltID(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1541
						order[1] = 1542
						order[2] = 0
						fix.Group.__init__(self, 1540, 1541, order)

			class NoRiskWarningLevels(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1560
					order[1] = 1561
					order[2] = 0
					fix.Group.__init__(self, 1559, 1560, order)

		class NoRelatedPartyIDs(fix.Group):
			def __init__(self):
				order = fix.IntArray(5)
				order[0] = 1563
				order[1] = 1564
				order[2] = 1565
				order[3] = 1514
				order[4] = 0
				fix.Group.__init__(self, 1562, 1563, order)

			class NoRelatedPartySubIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 1567
					order[1] = 1568
					order[2] = 0
					fix.Group.__init__(self, 1566, 1567, order)

			class NoRelatedPartyAltIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(4)
					order[0] = 1570
					order[1] = 1571
					order[2] = 1572
					order[3] = 0
					fix.Group.__init__(self, 1569, 1570, order)

				class NoRelatedPartyAltSubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1573
						order[1] = 1574
						order[2] = 0
						fix.Group.__init__(self, 1572, 1573, order)

			class NoRelatedContextPartyIDs(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 1576
					order[1] = 1577
					order[2] = 1578
					order[3] = 1579
					order[4] = 0
					fix.Group.__init__(self, 1575, 1576, order)

				class NoRelatedContextPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1580
						order[1] = 1581
						order[2] = 0
						fix.Group.__init__(self, 1579, 1580, order)

			class NoRelationshipRiskLimits(fix.Group):
				def __init__(self):
					order = fix.IntArray(7)
					order[0] = 1583
					order[1] = 1584
					order[2] = 1585
					order[3] = 1586
					order[4] = 1587
					order[5] = 1613
					order[6] = 0
					fix.Group.__init__(self, 1582, 1583, order)

				class NoRelationshipRiskInstruments(fix.Group):
					def __init__(self):
						order = fix.IntArray(26)
						order[0] = 1588
						order[1] = 1589
						order[2] = 1590
						order[3] = 1591
						order[4] = 1592
						order[5] = 1593
						order[6] = 1596
						order[7] = 1597
						order[8] = 1598
						order[9] = 1599
						order[10] = 1600
						order[11] = 1601
						order[12] = 1602
						order[13] = 1603
						order[14] = 1604
						order[15] = 1605
						order[16] = 1606
						order[17] = 1607
						order[18] = 1608
						order[19] = 1609
						order[20] = 1610
						order[21] = 1618
						order[22] = 1619
						order[23] = 1611
						order[24] = 1612
						order[25] = 0
						fix.Group.__init__(self, 1587, 1588, order)

					class NoRelationshipRiskSecurityAltID(fix.Group):
						def __init__(self):
							order = fix.IntArray(3)
							order[0] = 1594
							order[1] = 1595
							order[2] = 0
							fix.Group.__init__(self, 1593, 1594, order)

				class NoRelationshipRiskWarningLevels(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1614
						order[1] = 1615
						order[2] = 0
						fix.Group.__init__(self, 1613, 1614, order)

			class NoPartyRelationships(fix.Group):
				def __init__(self):
					order = fix.IntArray(2)
					order[0] = 1515
					order[1] = 0
					fix.Group.__init__(self, 1514, 1515, order)

class SetupMonitorRequest(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("USMQ") )

	class NoMonitorIDs(fix.Group):
		def __init__(self):
			order = fix.IntArray(7)
			order[0] = 22058
			order[1] = 22060
			order[2] = 22061
			order[3] = 22059
			order[4] = 22062
			order[5] = 22063
			order[6] = 0
			fix.Group.__init__(self, 22057, 22058, order)

		class NoMonitorRows(fix.Group):
			def __init__(self):
				order = fix.IntArray(97)
				order[0] = 22064
				order[1] = 22065
				order[2] = 22066
				order[3] = 55
				order[4] = 65
				order[5] = 48
				order[6] = 22
				order[7] = 460
				order[8] = 1227
				order[9] = 1151
				order[10] = 461
				order[11] = 167
				order[12] = 762
				order[13] = 200
				order[14] = 541
				order[15] = 1079
				order[16] = 966
				order[17] = 1049
				order[18] = 965
				order[19] = 224
				order[20] = 225
				order[21] = 239
				order[22] = 226
				order[23] = 227
				order[24] = 228
				order[25] = 255
				order[26] = 543
				order[27] = 470
				order[28] = 471
				order[29] = 472
				order[30] = 240
				order[31] = 202
				order[32] = 947
				order[33] = 967
				order[34] = 968
				order[35] = 206
				order[36] = 231
				order[37] = 969
				order[38] = 1146
				order[39] = 996
				order[40] = 1147
				order[41] = 1191
				order[42] = 1192
				order[43] = 1193
				order[44] = 1194
				order[45] = 1195
				order[46] = 1196
				order[47] = 1197
				order[48] = 1198
				order[49] = 1199
				order[50] = 1200
				order[51] = 201
				order[52] = 1244
				order[53] = 1242
				order[54] = 997
				order[55] = 223
				order[56] = 207
				order[57] = 970
				order[58] = 971
				order[59] = 106
				order[60] = 348
				order[61] = 349
				order[62] = 107
				order[63] = 350
				order[64] = 351
				order[65] = 691
				order[66] = 667
				order[67] = 875
				order[68] = 876
				order[69] = 873
				order[70] = 874
				order[71] = 1435
				order[72] = 1439
				order[73] = 1449
				order[74] = 1450
				order[75] = 1451
				order[76] = 1452
				order[77] = 1457
				order[78] = 1458
				order[79] = 1478
				order[80] = 1479
				order[81] = 1480
				order[82] = 1481
				order[83] = 1482
				order[84] = 218
				order[85] = 22048
				order[86] = 220
				order[87] = 221
				order[88] = 222
				order[89] = 662
				order[90] = 663
				order[91] = 699
				order[92] = 761
				order[93] = 22067
				order[94] = 22068
				order[95] = 58
				order[96] = 0
				fix.Group.__init__(self, 22063, 22064, order)

			class NoSecurityAltID(fix.Group):
				def __init__(self):
					order = fix.IntArray(3)
					order[0] = 455
					order[1] = 456
					order[2] = 0
					fix.Group.__init__(self, 454, 455, order)

			class NoEvents(fix.Group):
				def __init__(self):
					order = fix.IntArray(6)
					order[0] = 865
					order[1] = 866
					order[2] = 1145
					order[3] = 867
					order[4] = 868
					order[5] = 0
					fix.Group.__init__(self, 864, 865, order)

			class NoInstrumentParties(fix.Group):
				def __init__(self):
					order = fix.IntArray(5)
					order[0] = 1019
					order[1] = 1050
					order[2] = 1051
					order[3] = 1052
					order[4] = 0
					fix.Group.__init__(self, 1018, 1019, order)

				class NoInstrumentPartySubIDs(fix.Group):
					def __init__(self):
						order = fix.IntArray(3)
						order[0] = 1053
						order[1] = 1054
						order[2] = 0
						fix.Group.__init__(self, 1052, 1053, order)

			class NoComplexEvents(fix.Group):
				def __init__(self):
					order = fix.IntArray(9)
					order[0] = 1484
					order[1] = 1485
					order[2] = 1486
					order[3] = 1487
					order[4] = 1488
					order[5] = 1489
					order[6] = 1490
					order[7] = 1491
					order[8] = 0
					fix.Group.__init__(self, 1483, 1484, order)

				class NoComplexEventDates(fix.Group):
					def __init__(self):
						order = fix.IntArray(4)
						order[0] = 1492
						order[1] = 1493
						order[2] = 1494
						order[3] = 0
						fix.Group.__init__(self, 1491, 1492, order)

					class NoComplexEventTimes(fix.Group):
						def __init__(self):
							order = fix.IntArray(3)
							order[0] = 1495
							order[1] = 1496
							order[2] = 0
							fix.Group.__init__(self, 1494, 1495, order)

class SetupMonitorRequestAck(Message):
	def __init__(self):
		Message.__init__(self)
		self.getHeader().setField( fix.MsgType("USMQK") )
