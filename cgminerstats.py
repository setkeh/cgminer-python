#!/usr/bin/env python2.7

from pga0 import *
from cgminerversion import *
from cgminerconfig import *
from coin import *
from pga1 import *

print "CGMiner:"
print "Cgminer Version:", cg_version()
print "Api Version:", api_version()
print "PGA's Connected:", pga_count()
print "ASIC's Connected:", asic_count()
print "Pool Count:", pool_count()
print "Pool Stratergy:", pool_stratergy()
print "Miner OS:", miner_os()
print ""

print "Bitcoin Status:"
print "Hash Method:", hash_method()
print "Block Hash:", current_block_hash()
print "Long Poll:", long_poll()
print "Network Diff:", diff()
print""

print "PGA 0:"
print p0_mhs(), "MH/s"
print "Accepted Shares:", p0_accepted()
print "Rejected Shares:", p0_rejected()
print "Hardware Errors:", p0_hwerrors()
print "Utility:", p0_utility(),"/m"
print ""

print "PGA 1"
print p1_mhs(), "MH/s"
print "Accepted Shares:", p1_accepted()
print "Rejected Shares:", p1_rejected()
print "Hardware Errors:", p1_hwerrors()
print "Utility:", p1_utility(),"/m"
