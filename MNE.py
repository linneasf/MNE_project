#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:02:36 2019

@author: sepeforrestl2
"""

import mne 

raw = mne.io.read_raw_ctf('/Users/sepeforrestl2/Downloads/MNE_Gambling/MEG/KVHQBMJG_gambling_20190322_03.ds')

#picks= mne.pick_types(raw.info, meg=False, stim=True)
event_id= {'win': 32, 'loss': 33, 'boost': 34}

events= mne.find_events(raw, stim_channel='UPPT001')

epoch = mne.Epochs(raw, events, event_id=event_id, tmin=-.2, tmax=.2, preload=True)

epoch.pick_types(ref_meg=False)

# epoch.plot()
evoked_win = epoch['win'].average()
evoked_win.plot()
evoked_win.plot_topomap()

#thanks tom for being helpful unlike Fred 
