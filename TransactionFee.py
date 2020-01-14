from bitcoin.rpc import RawProxy
import sys

p = RawProxy()

txid = sys.argv[1]

raw_tx = p.getrawtransaction(txid)
decoded_tx = p.decoderawtransaction(raw_tx)

output_total = 0
for out in decoded_tx['vout']: 
	output_total += out['value']

input_value = 0
for input in decoded_tx['vin']:
	input_txid = input['txid']
	input_vout = input['vout']
	raw_input_tx = p.getrawtransaction(input_txid)
	decoded_input_tx = p.decoderawtransaction(raw_input_tx)
	input_value += decoded_input_tx['vout'][input_vout]['value']

fee = input_value - output_total

print "Transaction's ",txid," fee was ",fee," BTC"