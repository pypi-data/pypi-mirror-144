from nfstream import NFStreamer, NFPlugin
import numpy as np
from scapy.all import IP, IPv6, rdpcap, raw


class NBytesPerPacket(NFPlugin):
    '''
        Extracts the first n_bytes from each packet in the flow, the bytes are taken
        from the transport layer payload (L4). if the flow have less than n_bytes bytes,
        then the rest of the bytes are zero-valued.
        
        remove_empty_payload flag tells the plugin to do not add empty payload packets such as acks in TCP.
        max_packets param determines the highest amount of packets to save/extract from flow.
    '''
    def __init__(self, n=100, remove_empty_payload=True, max_packets=2):
        self.n = n
        self.remove_empty_payload = remove_empty_payload
        self.max_packets = max_packets
    
    def on_init(self, packet, flow):
        flow.udps.n_bytes_value = self.n
        flow.udps.n_bytes_per_packet = list()
        flow.udps.n_bytes_curr_packets = 0
        
        self.on_update(packet, flow)

    def on_update(self, packet, flow):
        if packet.payload_size == 0 and self.remove_empty_payload == True:
            return
        
        if self.max_packets is not None and flow.udps.n_bytes_curr_packets == self.max_packets:
            return
        
        amount_to_copy = min(self.n, packet.payload_size)
        if amount_to_copy == 0:
            flow.udps.n_bytes_per_packet.append([int(i) for i in list(np.zeros(self.n))])
            flow.udps.n_bytes_curr_packets += 1
            return
        
        max_index_to_copy = -packet.payload_size+amount_to_copy if -packet.payload_size+amount_to_copy != 0 else None
        n_bytes = np.zeros(self.n)
        try:
            n_bytes[:amount_to_copy] = np.frombuffer(self.get_payload_as_binary(packet, flow.ip_version)[-packet.payload_size:max_index_to_copy], dtype=np.uint8)
        except:
            print('err')
        flow.udps.n_bytes_per_packet.append([int(i) for i in list(n_bytes)])
        flow.udps.n_bytes_curr_packets += 1
        
        
    def on_expire(self, flow):
        # todo: add byte normalization
        if self.max_packets is not None and flow.udps.n_bytes_curr_packets < self.max_packets:
            for i in range(self.max_packets - flow.udps.n_bytes_curr_packets):
                empty_buffer = np.zeros(self.n)
                flow.udps.n_bytes_per_packet.append([int(i) for i in list(empty_buffer)])


    def get_payload_as_binary(self, packet, ip_version):
        if ip_version == 4:
            scapy_packet = IP(packet.ip_packet)
        elif ip_version == 6:
            scapy_packet = IPv6(packet.ip_packet)
        
        return raw(scapy_packet.payload.payload)
        