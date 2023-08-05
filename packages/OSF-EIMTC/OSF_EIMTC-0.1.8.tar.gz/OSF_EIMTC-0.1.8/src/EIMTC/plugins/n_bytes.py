from nfstream import NFStreamer, NFPlugin
import numpy as np
from scapy.all import IP, IPv6, raw

class NBytes(NFPlugin):
    '''
        Extracts the first n_bytes from the flow, the bytes are taken
        from the transport layer payload (L4). if the flow have less than n_bytes bytes,
        then the rest of the bytes are zero-valued (padding).
    '''
    def __init__(self, n=784):
        self.n = n
    
    def on_init(self, packet, flow):
        flow.udps.n_bytes_value = self.n
        flow.udps.n_bytes = [] # np.zeros(self.n)
        flow.udps.n_bytes_counted = 0
        
        self.on_update(packet, flow)

    def on_update(self, packet, flow):
        remaining_bytes = self.n - flow.udps.n_bytes_counted
        if remaining_bytes >= 0 and packet.protocol in [6, 17]: # TCP or UDP only.
            amount_to_copy = min(remaining_bytes, packet.payload_size)
            if amount_to_copy == 0:
                return
           
            flow.udps.n_bytes.extend(
                self.get_payload_as_binary_scapy(packet, packet.ip_version)[:amount_to_copy]
            )
            flow.udps.n_bytes_counted += amount_to_copy

    def on_expire(self, flow):
        '''
        Normalize to [0,1]: 
        flow.udps.n_bytes /= 255
        Optional cleanup: 
        del flow.udps.n_bytes_counted
        '''
        # Padding if necessary.
        if flow.udps.n_bytes_counted < self.n:
            remaining_bytes = self.n - flow.udps.n_bytes_counted
            flow.udps.n_bytes.extend(
                np.full(remaining_bytes, 0)
            )

    def get_payload_as_binary(self, packet):
        return packet.ip_packet[-packet.payload_size:]
    
    def get_payload_as_binary_scapy(self, packet, ip_version):
        '''
        Older versions of NFStream (lower than 6.1) had problems with 
        detection the correct payload size of ipv6 packets.
        This function is here as a fallback in case of problems in future
        versions.

        in 6.4.2 and 6.4.3 there is a bug with wrong transport_size, also
        NFStream does not detect ethernet padding.
        '''
        if ip_version == 4:
            scapy_packet = IP(packet.ip_packet)
        elif ip_version == 6:
            scapy_packet = IPv6(packet.ip_packet)

        return raw(scapy_packet.payload.payload)
        
