#!/usr/bin/python
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Library General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# DUBDecoderTest.py
# Copyright (C) Simon Newton

"""Test cases for the DUBDecoder class."""

__author__ = 'nomis52@gmail.com (Simon Newton)'

import unittest
from DUBDecoder import DecodeResponse

class UIDTest(unittest.TestCase):
  TEST_DATA = [
      0xfe, 0xfe, 0xfe, 0xfe,
      0xaa, 0xaa, 0x55, 0xab,
      0xf5, 0xaa, 0x55, 0xaa,
      0x57, 0xaa, 0x55, 0xaa,
      0x75, 0xae, 0x57, 0xbf,
      0xfd
  ]

  TEST_BAD_DATA = [
      0xfe, 0xfe, 0xfe, 0xfe,
      0xaa, 0xaa, 0x55, 0xab,
      0xf5, 0xaa, 0x55, 0xaa,
      0x57, 0xaa, 0x55, 0xaa,
      0x75, 0xae, 0x57, 0xbf,
      0xff  # invalid checksum
  ]

  def testInvalid(self):
    self.assertIsNone(DecodeResponse(bytearray()))
    self.assertIsNone(DecodeResponse([0]))
    self.assertIsNone(DecodeResponse([0, 0, 0]))
    self.assertIsNone(DecodeResponse(self.TEST_DATA[0:-1]))
    self.assertIsNone(DecodeResponse(self.TEST_DATA[4:]))
    self.assertIsNone(DecodeResponse(self.TEST_BAD_DATA))

  def testValidResponse(self):
    uid = DecodeResponse(self.TEST_DATA)
    self.assertIsNotNone(uid)
    self.assertEquals(0x00a1, uid.manufacturer_id)
    self.assertEquals(0x00020020, uid.device_id)

if __name__ == '__main__':
  unittest.main()