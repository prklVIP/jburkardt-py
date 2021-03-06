#!/usr/bin/env python

def cycle_brent_test04 ( ) :

#*****************************************************************************80
#
## CYCLE_BRENT_TEST04 tests CYCLE_BRENT for F4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
  from f4 import f4
  from cycle_brent import cycle_brent

  print
  print 'CYCLE_BRENT_TEST04'
  print '  Test CYCLE_BRENT for F4().'
  print '  f4(i) = mod ( 31421 * i + 6927, 65536 ).'

  x0 = 1
  print
  print '  Starting argument X0 = %d' % ( x0 )

  [ lam, mu ] = cycle_brent ( f4, x0 )

  print
  print '  Reported cycle length is %d' % ( lam )
  print '  Expected value is 65536'
  print
  print '  Reported distance to first cycle element is %d' % ( mu )
  print '  Expected value is 0'

  return

if ( __name__ == '__main__' ):
  cycle_brent_test04 ( )
