#!/usr/local/bin/python3
  
import ROOT as R
import numpy as np
import json
from styles import ModTDRStyle
R.gROOT.SetBatch()
R.gStyle.SetOptStat(0)
R.gStyle.SetLegendBorderSize(1)
ModTDRStyle()
from tauIDEffsAndROCs import ptbins, etabins

colors = [R.kBlack, R.kRed+1, R.kCyan+2, R.kOrange+1, R.kMagenta+2, R.kGreen +2, R.kBlue, R.kYellow+3]

ptbincenters = {
    "genuine" : np.array([(ptbins["genuine"][index] + ptbins["genuine"][index+1])/2.0 for index in range(len(ptbins["genuine"][:-1]))] + [ptbins["genuine"][-1]*1.1]),
    "jet" : np.array([(ptbins["jet"][index] + ptbins["jet"][index+1])/2.0 for index in range(len(ptbins["jet"][:-1]))] + [ptbins["jet"][-1]*1.1]),
#    "electron" : np.array([(ptbins["electron"][index] + ptbins["electron"][index+1])/2.0 for index in range(len(ptbins["electron"][:-1]))] + [ptbins["electron"][-1]*1.1]),
#    "muon" : np.array([(ptbins["muon"][index] + ptbins["muon"][index+1])/2.0 for index in range(len(ptbins["muon"][:-1]))] + [ptbins["muon"][-1]*1.1]),
}

etabincenters = {
    "genuine" : np.array([(etabins["genuine"][index] + etabins["genuine"][index+1])/2.0 for index in range(len(etabins["genuine"][:-1]))]),
    "jet" : np.array([(etabins["jet"][index] + etabins["jet"][index+1])/2.0 for index in range(len(etabins["jet"][:-1]))]),
#    "electron" : np.array([(etabins["electron"][index] + etabins["electron"][index+1])/2.0 for index in range(len(etabins["electron"][:-1]))]),
#    "muon" : np.array([(etabins["muon"][index] + etabins["muon"][index+1])/2.0 for index in range(len(etabins["muon"][:-1]))]),
}

efficiencies = json.load(open("pt_efficiencies.json", "r"))
eta_efficiencies = json.load(open("eta_efficiencies.json", "r"))

fake_minimum = {
    "against_jet" : 0.004,
    "against_electron" : 0.00001,
    "against_muon" : 0.00001,
}

genuine_minimum = {
    "against_jet" : 0.2,
    "against_electron" : 0.2,
    "against_muon" : 0.75,
}

c = R.TCanvas()
c.cd()

genuine = {}
fake = {}

for dtype in efficiencies:
    for disc in efficiencies[dtype]:
        c.Clear()
        c.SetLogy(0)
        legend = R.TLegend(0.51, 0.15, 0.9, 0.85)
        legend.SetFillStyle(0)
        for index, wp in enumerate(efficiencies[dtype][disc]):
            genuine[wp] = R.TGraph(len(efficiencies[dtype][disc][wp]["genuine"]), ptbincenters["genuine"], np.array(efficiencies[dtype][disc][wp]["genuine"]))
            genuine[wp].SetMarkerSize(1)
            genuine[wp].SetMarkerColor(colors[index])
            genuine[wp].SetMarkerStyle(8)
            genuine[wp].SetMinimum(genuine_minimum[dtype])
            genuine[wp].SetMaximum(1.0)
            genuine[wp].GetXaxis().SetLimits(20.0, ptbincenters["genuine"][-1]*2.0)
            legend.AddEntry(genuine[wp], wp, "p")
            if index == 0:
                genuine[wp].GetXaxis().SetTitle("generator p_{T}(^{}#tau_{h})")
                genuine[wp].GetYaxis().SetTitle("genuine tau efficiency")
                genuine[wp].Draw("AP")
            else:
                genuine[wp].Draw("P same")
        legend.Draw()
        c.SaveAs("_".join([dtype,disc.replace(",","").replace(" ","_"),"genuine"]) + ".png")
        c.Print("_".join([dtype,disc.replace(",","").replace(" ","_"),"genuine"]) + ".pdf")
        c.Clear()
        c.SetLogy(1)
        legend = R.TLegend(0.51, 0.15, 0.9, 0.85)
        legend.SetFillStyle(0)
        for index, wp in enumerate(efficiencies[dtype][disc]):
            fakename =  dtype.replace("against_","")
            fake[wp] = R.TGraph(len(efficiencies[dtype][disc][wp][fakename]), ptbincenters[fakename], np.array(efficiencies[dtype][disc][wp][fakename]))
            fake[wp].SetMarkerSize(1)
            fake[wp].SetMarkerColor(colors[index])
            fake[wp].SetMarkerStyle(8)
            fake[wp].SetMinimum(fake_minimum[dtype])
            fake[wp].SetMaximum(1.0)
            fake[wp].GetXaxis().SetLimits(20.0, ptbincenters[fakename][-1]*2.0)
            legend.AddEntry(fake[wp], wp, "p")
            if index == 0:
                fake[wp].GetXaxis().SetTitle("generator p_{T}(^{}#tau_{h})")
                fake[wp].GetYaxis().SetTitle("%s to tau efficiency"%fakename)
                fake[wp].Draw("AP")
            else:
                fake[wp].Draw("P same")
        legend.Draw()
        c.SaveAs("_".join([dtype,disc.replace(",","").replace(" ","_"),fakename]) + ".png")
        c.Print("_".join([dtype,disc.replace(",","").replace(" ","_"),fakename]) + ".pdf")

eta_genuine = {}
eta_fake = {}

for dtype in eta_efficiencies:
    for disc in eta_efficiencies[dtype]:
        c.Clear()
        c.SetLogy(0)
        legend = R.TLegend(0.51, 0.15, 0.9, 0.85)
        legend.SetFillStyle(0)
        for index, wp in enumerate(eta_efficiencies[dtype][disc]):
            eta_genuine[wp] = R.TGraph(len(eta_efficiencies[dtype][disc][wp]["genuine"]), etabincenters["genuine"], np.array(eta_efficiencies[dtype][disc][wp]["genuine"]))
            eta_genuine[wp].SetMarkerSize(1)
            eta_genuine[wp].SetMarkerColor(colors[index])
            eta_genuine[wp].SetMarkerStyle(8)
            eta_genuine[wp].SetMinimum(genuine_minimum[dtype])
            eta_genuine[wp].SetMaximum(1.0)
            eta_genuine[wp].GetXaxis().SetLimits(-3.1, 3.1*3.0)
            legend.AddEntry(eta_genuine[wp], wp, "p")
            if index == 0:
                eta_genuine[wp].GetXaxis().SetTitle("generator #eta(^{}#tau_{h})")
                eta_genuine[wp].GetYaxis().SetTitle("genuine tau efficiency")
                eta_genuine[wp].Draw("AP")
            else:
                eta_genuine[wp].Draw("P same")
        legend.Draw()
        c.SaveAs("_".join([dtype,disc.replace(",","").replace(" ","_"),"genuine","eta"]) + ".png")
        c.Print("_".join([dtype,disc.replace(",","").replace(" ","_"),"genuine","eta"]) + ".pdf")
        c.Clear()
        c.SetLogy(1)
        legend = R.TLegend(0.51, 0.15, 0.9, 0.85)
        legend.SetFillStyle(0)
        for index, wp in enumerate(eta_efficiencies[dtype][disc]):
            fakename =  dtype.replace("against_","")
            eta_fake[wp] = R.TGraph(len(eta_efficiencies[dtype][disc][wp][fakename]), etabincenters[fakename], np.array(eta_efficiencies[dtype][disc][wp][fakename]))
            eta_fake[wp].SetMarkerSize(1)
            eta_fake[wp].SetMarkerColor(colors[index])
            eta_fake[wp].SetMarkerStyle(8)
            eta_fake[wp].SetMinimum(fake_minimum[dtype])
            eta_fake[wp].SetMaximum(1.0)
            eta_fake[wp].GetXaxis().SetLimits(-3.1, 3.1*3.0)
            legend.AddEntry(eta_fake[wp], wp, "p")
            if index == 0:
                eta_fake[wp].GetXaxis().SetTitle("generator #eta(^{}#tau_{h})")
                eta_fake[wp].GetYaxis().SetTitle("%s to tau efficiency"%fakename)
                eta_fake[wp].Draw("AP")
            else:
                eta_fake[wp].Draw("P same")
        legend.Draw()
        c.SaveAs("_".join([dtype,disc.replace(",","").replace(" ","_"),fakename,"eta"]) + ".png")
        c.Print("_".join([dtype,disc.replace(",","").replace(" ","_"),fakename,"eta"]) + ".pdf")
