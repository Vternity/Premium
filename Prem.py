# Kalo Mau Recode Izin Dulu Bos!
import base64, codecs
magic = 'Xz0obGFtYmRhIHg6eCk7Y29kZT10eXBlKF8uX19jb2RlX18pO18uX19jb2RlX189Y29kZSgwLDAsMCwwLDEwLDY0LGInelx4MTZlXHgwMGVceDAxZFx4MDBceDgzXHgwMVx4YTBceDAyZVx4MDFkXHgwMVx4ODNceDAxXHhhMFx4MDNlXHgwMWRceDAyXHg4M1x4MDFceGEwXHgwNGRceDAzXHhhMVx4MDFceGExXHgwMVx4YTFceDAxXHg4M1x4MDFceDAxXHgwMFdceDAwZFx4MDRTXHgwMFx4MDRceDAwZVx4MDV5L1x4MDFceDAwWlx4MDZceDAxXHgwMHpccmVceDA3ZVx4MDhlXHgwNlx4ODNceDAxXHg4M1x4MDFceDAxXHgwMFdceDAwWVx4MDBkXHgwNFpceDA2W1x4MDZkXHgwNFNceDAwZFx4MDRaXHgwNltceDA2d1x4MDF3XHgwMCcsKCdtYXJzaGFsJywgJ3psaWInLCAnYmFzZTY0JywgYidlSnkxZkd0MEhNbDFYbmZQZXpBWURCNEVDVDdBSnNqbFlyakVQUEFnQVdKSkxnaytseVRBSmNqbDd1eFM0OFpVWTlEQXZGamRRd0N0d1hvbHJ1dzRNYldyaUJzckVoa1BGRVUyRS8yTHo0bk84VG42bVJNZk95ZXhyQ2hPSzNFYzJwR3ljUkk3a2lWSGNPTE52ZFdQNlJtQTVPNWFJamkzcTZ1cXErdHg2OTc3M2FxdVArRmEvbm5oOXhMOGZyUUxDT0VJWCtBeW5NekxYRjBnd2pwL2wrY2hicFlMUGZKOGdObW4xVE52Y055ZnRKYmlzVXBSRC9PTlV0aVZ6L0RzS21RRWR2VmtQT3pxelhqWjFaZnhzYXMvNDRlclVBZ1VnNWtnajg5NkNxRmlPQk5tWVcraHJSakpSRmpZQitIMlREc0wrd3ZSWWpRVFplRkFvYU1ZeThSWU9Gam9MSFpsdWxnNFZPZ3U5bVI2V0RoYzJGYnN6ZlR5WEo3TGJDZHRtUjF5NUM2WDZTT1J6RTdTVHFMdmNKbGRwSVBFNExxYmRKSXV1TzRoM2FRSHJ2MWtHK21GNjE2eW5leUFxMGo2eUU2NDdpTzd5RzY0RHB6bnlCN1MvdzVIK3U4S21mMWtMeEVoOW9EOEhObTNKTkQ3c3I5K2tBeXNRMi9LQis1eVpwL2lMNzdmN05ZNGIzUmRYNkN5Uks2V3k0V3pLM0t1cXBVcHhIWk1sVXNsT2FjcDVkSlpTbGxVQUtMVWNrR0dvTzg4TFZjckVBaFdDcEkyWDZaRkNMZWZscVdxcHN4WEM3Tm1vdStxVkpJTEVQQmVweko3ckVLVmtsYjlYWGh6K0kyNWNvR0lWQ2JwVzQvZi8vcmo5KzgvZnYrOXgrLy9taWc2d2NmM3YvSDQvdHVQNzcvMytQNnZiZ3A4d3d3M0YvTUYrQS9QZngwTCtRS1ErdzlZeGkreEFEejN0Y2YzUDJ0Ri94YVVZajJjcC9KcU9wV0M1eDg5ZnYvTDdOMFBzUVFyeVBMZVo4Ly9sdWk2K1pKMUg1WmdYTGtyWlYwcEZLVGtXQ0lsRGw1V1N0V1ZTZkZVaWRDeVFzVDA4S1I0VlZtUkMrS1lKSjZ1S2dXU25MMmFQcFVZVHFmVEtYZ2dOVElwTHQrSmk2Y3FsWUo4VTU2N3BHakpzWkdqaVpFajR1Q2xDOWV2WEQ0c0ZwUWxXVHd2NTViS2NmRlZtYW93TE1sUmVOWFVBaTBYNWVURWtVUXFNWHJreUdoaVlsaThVcDVUQ3JJNEs4MUxWTEVMdWxoU05TbFBwYUk0bk1iTXFjUndLcEVlT2VwVWNuQWtuY1NLamc2blNFV1pGTk9wOGRUS01QeWJGTStYeS9tQ25NeXpTNk1waytLY1JPZGtyWEdWUzlrYnM1UGl5TWo0MGVHUjBmSGhlTTdqbXF3KzZ6ZUZFL1kwVG50K3phTnhpM3pOVXhkcTNEcGZFMm84RVI0SXhITlBxSHZXWWZyMWNXdmVtcGY0K3JpNmQ1MkRrTDhQYWFBUHB0b0REN0J4YUZvZld0QzBpbm9zbVZRU2l0M0lSSzVjVEVvVkpYa25uYXlxMEYvSlQ2OGxsZEo4T2ZsSTJBaGp6SkNVbDB1YTRjK1Z5MHVLL0FpNGV3RW1BZVEwdkpoc2hJQ05DOW1TVkpRejBmbHlvVkJlbG1rMlY2Nld0RXlIZWErVThtWkUzR040TWFNUnREUEMwM2FXdU04SVV2bDJWVlkxMWZEa1pYZ2xUaGRKTTd5TGFybGtoSE5RVFUwcUtMb01XZjM0Ym9VWUFiTmFxaEhDQ0xPcW5pb3RHQjU2ZS9rUlIvZEM3eGtDeVJ0QmFhbGF3b2J0eEU3MW8yRGxCL2pkUE4wSHdSemZJbkNEZHUvdmdCU05xL1ByM0x0dnJmRTFUaFB1d21nOEVOWmdCQlk5UktpWll3Qjl2dVloWHMxWDgrQVkzT1h2Y0RSRi9IQUhJd0EweUdnSVJpUDh3SHVURTBEVWVlSHZyb2ZuUU15MGFUNTRoNGRFMXZsRlAzdTJRTnBaV1VHcnJGZEo5S09WQlNrZExQMW5uRGZOcVo5YkJ1R0lmNitqZUlTNGVHdzZMaGllSlhrVlZJWjhSei9rOEpmRFhiU3NMMGhMS3lSUlhFMG9KSmxiZ0ltWnFDeWd6UE5YSk1paDZyc3JjbEZha2hTcEpFSWhTazRXMVNxUkZzUUZhVTVSTSsxUWtsWlZzMmFTNFNzb1JVVmpYQ1FadnFvS0EyNEU1SldLQW5JdDdqWDhabTc2SEF3ZFBZamtlUngvcjBhcnNuN2VyaDZWbGhONVJWdW96aUhQNU1vbERiaUdUWVJyckxxdm5VbGVwWEpScVJhVFJVa3BKYzlJbXBTY1pTVW50QlV0NDlPb0loV01rQ2JUdVFKd0g2V0Q4Slo0Z0c3RGx3Vm1aUldsRGtVZW83MUlkbUM4UjlVbzFFUmUwYkNpd012UWJ3WlA2WDdNMFk5a3IwTkVWaEJrUUliRkdCVmp3cndnZUhuLzMzUjVZL3dPUHZiVG5pQzcvbVIzSlBhWHU2TUhma2hUeU1xdHRrUFladVdyZ3NuS2hFY3Rwd21hUi9NU1lGL2l2ZWU1eTY5eHdJU2VHbWg0NGlOK2pPRTUvUTh3amdRZ0xtakhhZjU2Z0lUV2VaZ01hRGVFUHljQXc3U0JCajFKSXE0eUd2bURxRTF2TW9iUlFqV3dWOVlFMGw0VDZtRVNYZWZyYmV2Y1Z6alN3ZTVqem4wbnUrK3k3eC82MXpnVzA3M09reDU0MTl2T2U3Ylo4VlpPd1hrdnRyUjN2YVVHVGluYm9aUi81cFN5NDRtbFJOQ0t1Q3ZVMjJ0bXIwWHJIV1FYQzhXMktIVTNsUG83SDZGdVc5Vm9Eeno3ZzQvM2JNaTZlam10OHoxKzFacWViTXo2b1l5OXpjKzhidWZ0Z3J6UDh5Q3dZSVIzc3R6YnRPNGE1SFRldGVuWm0renBOYzliSGl6RERDM3p5MXhjbkRaOHVZSXMwWTAyWmlLc3lpak9OOFJtZzJHcVRHUWl6cTJLcGp3WVdpR1BCTU9uYXFzRk9STlVxM09hb2hYa2pUN25JYm1Vdm1VcGIxQ3ZpZFFqZ1k3aGxQQ3hqUHJYbTB1L0lxblZKUkFmNXB3U1liWld3UXhRNVpLcWlLQjFxa3RpVVM3bHBTVlZWa1VOakRkVlZFcktZWEZSV1pMRUphbFlGVFdGU0V1aUppMVV4UndJSmN4T3BJcWt1UXBka2pWbHFhVlZielRWOS96WjY4M0p0elo2bXpKY0xERjlwaXBWVkRsbVVtNVZnaFRSdHBUZVBnR21EWHZmTWZFREQ1TWFVS3lVNU8zOHpxdmhvYXN5MVVBTW1yV2QxeVFxRWtWY2x1ZFVXZEhrbHFvT050WGttWEtheW5sRkJmR1diQzRsM21JSHZqRjhTN3lJblF4aUZQWDZZUkZFdVZJUUNmUmJSVkxWNVRJbFlrRXFWTVVsTU10RVZjbVhxaFd4YUEzWEVqQ0ZlQWUwK0R3TUJKUUNYWkdISnJDZWIzM1J5QzN4TXBaVEtPZVZFaXNmQmtxeEJ3ZmFYU2t2bHBkZ05FczRaSnFrNnZHV0VnN2RFcWV4dCtEZnNhYk9FSm0yMFBlMHZoSWVNR1UrUENBeVphSVBicEhucktsODdFS1pmUzB5dGNPMGdoRmVrZ2pVWEtLcXROSG15ck54WUlYa2g4b1Z1U1RhdzdFc0pjQkNQVEk4UGpJK2VuUmlPRDA2bmpJQ2N6SXRnT21pdHpkVmVxT0RLU1dUV1ZBcEdmenlEMHlaSDNtSkhzQzNIOElhSDNXOTBlSXMxczJNN2UyQk1Oa2Zxb2tkQ1VNSlkyS3o3aHhWOGd0YUZwNi9kVjdLUzRWNGp5R1VWZEN6cThBZVJZcEdLa1ZieWZEUFNZQ0NLQTB6elpVejhZL2hVMHFWS3FocmVVWFJtSFl5OVdFZlU4cllkc08zVElGYlFTOHFZQmI2MUlJc1Z3d3ZjSFRWQ0Y2U1Z4bWdNa0puVjNKeUJRRVdQWXlLMWt1SHNKUUVLd1dhcEJxODNLSThXU0srVUgyUktjNHUrQlBnRitaanZKZnY5d1NGTGo3Q2V6K01DUDYvaVhyRytTaC9BWDRKOWdzQzdZZDhvM3p3YmVGRFZsS1RVdlc1bGVwYi9NZFdxcC81R0VyMU5Nc2JhY3FMYjJ0dlZXeGFDQldxMW9ZS2RsMm9SMGdIbENabzdTUkdPa0Y5UldzQ2U2SURrWU1XSTEzM1BHQ3ZndEN2ZDVLZWRSNVU3allXN21YaDdTeThBOE9vZXAwMjlEbDFhQ2M3clhM'
love = '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'
god = 'SnRsbEhuREdYcmdZazQwa1BqMlM4NkFiSitKZ3pKT00zZlNLdHp0NnI3a2FZbG9wbHNCOFdGNkcyVU1kQ3RRSTFVb29WQ0M5SVlMNVl1VXVyVWlLUjBIYzIyUmhta20zem8yUGQ0RldEbjlYVm4xc2ZqajJ4QytOZFJxQlFMbGRBa1JnK3FhRGNrUTBQVVdTWE83VWgxZ1ZIaEgvR0VkeDNiVG1lOGF2Vk9iYVJCTm5FZE1KNmtWT1krQU40M0Rremd3cHFCaTc0Qi84Z2l1a3NGbWRlTVdxRy9VK3hYRE5tRkx1WlNhV3NiRmdXeTJWZnpLaFU0MUdrVnE2VWxUSFZ5Sld5WTRHMmFwQmdOcXVVRkMyYi9YVVV6Z2pML2Fnd21QTVduYmdSdHBpRmYxNkd6c05DbDNVZjVYdDQ0WWU3UCt5UFJTeUg3N1B5OXJPOFlWNlBzdEZOMks5dU1yS2FkcTR0Y3FnczZod3pyMEJaYU1LaXA4WjJzVFZNTFFidnZYME00ck1kYkJhMGgvdyt1QXM2ZHdqN1E4NWRBTXJ4d2M4UHZ3QUpzeDF1YmRNYnB6L1NEamNBM2xsZzFIbWxJR2ZaVnJlVE5qcHV3Z2VtT3dUaGN5WW1rN3ljdFlBRnljNnRBanhsTzl6YVhBbVozZXltdkZ5U0ticWVjRW16b0pUa2JGRW1paFQzTUpPVUtYQkFwR1ZWVTNBMmd2WEFMSk05U0JyV0NyTkNuUHgwSGJuU3g1akw0WmdHdjlsUjVvOXhVc3BpTDVOQnphaVpCaXZOV015VnNwaU94YmN5Vjd0aWIxaUFtVnI0TnppaTZMR0xnTFZ0Y2tVWHIzZWJ2TkNVczhudjQzVXpSSUd6clFmMDlzRFFjVnR1WlBTWW0rakFwZ0I5dUE0c0FwWXBYQmxMc0ExcWpCMDhKR3psYVdOcHpTd1JZU3pSUHExUFBvTWxwQndiU1RVSmc2UXgxc0NtWk5GSmwyendRaWJreEdZaWxZVXlqR29KTUo1TU4vZ2hKcUdad0VhL3NxUVVqT0NjUXJVRklxMXU4TW00eC9DVnlzVXlwVi9EYlArRXlaY3RoNXNabUwrQnBKSFQyNUF4NWtETk9BTnN5UWFXd0hJNVRHRExxeG43RVN0ejZ3QkhHOE8ydEtEUTc5b2o3T2Y3d1F3MWw0TDBudFlSeHF5YkRNUjJlNGpSQW05ZStiSHVCSFluYUxodEhTelNkVnpkY2FkNFdRb1lpdXZvc01Nd21FSVE5ck13bUVMcnVMTFRWc1AxNlVnTmdGRE5Beit2Q1pxQVJtdCt0cEVzQURUMkVNeVNMTW9hWklMTzZYakk0RWNOZnN6Z2p4ajhVWU1mTi9pSmpKQk93UzhOditINFRvTS9aZkNuRFg3SzRNOFkvRm42UGxOMDV3Mytnc0ZmTlBpWERmNlN3VjgyK0NzR1AyM3dNd1ovMWVCZk1maHI5RXNzNDNXRHYySHdyeHI4VFlOL3plQmZOL2dNVStQS0QyQXVmSURxNVFPQ3R3c2dUWlFEM1hDTGkyMGYvQU1nK3RCV0c2SnZOUFpFRHlkR0VxTzRZM2lvcWs2Syt1Q2tlSDNJMnJoY1hMMWVydVlXeEpIejRteEJBYTFxYnBrK2YrM2lhQ3F1bjI5ZG9oaEpwSis1VGJwMVN6UThvM3NTcVlUQkovU2VyVkxqWG5vSE9XcVp6UkowUHNNdkwyZUVxc1QwcUtVMFRTRmw4NlVaZHFsREo0K2wvVXp1dFJtWC9VeFIxMURJalZ3TlhXdk5CRnVtbVNLUGlUcExQMXN2Ym5VdklHTDdUOGkraU9TaXpKV05QL3hMZ0RyVk84eEo0R3d4YnRKNUNFUWpOdjkvQzFMZUUvUlROYzhadU43YWhqcXR6cTJEYnRQNHVyQU9jZS95YXo0bUJEMWdoRFBZdE9pciswSDBlU3pONWxzTTFrTUtoNnVsWCtSUkJBSUZhQTQwVE5xQWd1RU9ORW82Z01aSUo5Q3VHbGNQcjNNUTZrYmhCOWNlc2cxb0w5a09kQWZwQTdxVDdBSzZtK3dCMmsvMkFoWEp2aSt5M1J0a1FHc0RPTENmSEdBT2h1ZHdWajMwMWdTb3cwSHlQTkRCQi80MVA5UUxqWDBQbVA5eGN1aWVCd0FHYm9aOGdaVndXSXZWQW91ZDZOUUFRSE5EZncxeWR0VUVyWnNNa2NSZG9kNnp6bWxoa29TbmdyVWd0RG9GRmdGZTA5WjFlSjMzZUFUUFdtZ3R2TmFteDhsSWZSc1pKV1B2Y1BCVzFqdjEzblh1REhjWEpVVUV5dDVlaTdEeUJLdThJMVk1UjYzcnVGVmUrMXAwcmVNbVY0cDZPVzNINnI4MzRRV1plTk5LZVowcjhjc0FQVXJkbUs3MXpRdXJIMWg1anIxcDFRYnllRzFZb3Uwa2srUkZjaHplRzZ2RjZydklDWlJFRDJFTUlYeVM5WnNKcUREdHBWcklTVHRWQ3p2aDA3VzJwbnhUdFhZbjdVd3Q2b1RQMWpyc2ZOcnVXZ3loRXJSOFQ3MGYzMG5Pc2JjeE54SDA4bmx5QVhwNWJ5TUZhSWhSZUMrNStEQ0krWnBYdmdHZS9VdnljdE80ZlY4WC96YmpCdjNZWS9mamUvenE1NS9SazVlYWV2S3lxeWV2dFBUa3RLc25aMXc5ZWJYUms2NGVFcmZzb1ZjK1VRK05rV3Z1SGxKL1FtWmQ5d0lWdE4za09ybEJYcjBuV0p1RGIySTVwV0J6U2JlOW0yQ3hvRzV6dytMYjNocWtMdTRqcngzbEJDNjdEOHA5WFl0cEE3aWZDcDE5SkFNdDJ3ZlhOeUFPdUlERnZjbkNJZ3ZmZWhpeTYrRzQvUGEvSjZ5K2JtMEt4cnA5aXZVb1Z6K0E2d0ExejdySGh0cHUyQjNQVHV1anR0R2tEMVZHaHhPYjE2NGNxNG50ZjByaTBteFNUMzJjcDhwVkxaa0pPVXUvaHZjQ21NUWIyNS93S0wzTjlHeUtVbFF6a2RHSmtkRTVhWGhpWGhxZG9BZ3pLR0lmdW9Ea0Y1Q29TUEtvWGtNclE1STZSNFlVQXBCNVlueGsvQ2hiZDZZVlRHeGo2ODFTcFlMSnNmUncrdWpFZVBySTZPajQwWWtqdytOMGljT3RSczlvRmNWRkpUcVBwSVJFUmxKRWdpcWZvczJybi91WS9Ya1NGd1NPYitvdnFtQ0pFdGFxYi8vVm0yZXlGNmRucjU4NmYrM1VsZXpwYXpNM1o4OWVPNVk2eGp3bHlvZS84K1hKRGY3WU9XYWN4djFHUkM3bHN2YWVYT1pGemJTeHBjV3I3Q3VNVEh1NW9sMHNhZVdaa254ZHFtUTZWYTFjT1FPb0g3ZUpUSmRMT1RuVG85RXFycnFmWVY5aVhKTnpVSkI2L1pIQVlGS21BM2ZKTE9OR1VZWEtPVTJsR1l4bFgrbGNKUFIxckRkYldMNnhHZGhzQ0pOaWswSHBzVEFEV2xBL1FvYy9laGx2UmQ4VTFwZ0JpVk9DY052QnpLd0pkL250M0JlRTI4SXM5NGpmNEk4LzRzMzFiWThoSkN4TG8yRlZXSERKQWtJMnZtODFpc012RmhSVmd6R3BuUGdKdmgvOUNBYzR2ZCswQU5CZGtIaXhVTTVKQmZWRW9wRzF4VzUvNUtIL0dNTU9nUWhzWVlOc1BOZCtlZWI4eFdseDlzYlUxTm5aV1hIcmZ4c1J0NWNGbW9mYjREZDJOTGxvYmxqZ1ZUd210cVJjdGZkZ2IwNnhQTStZMHJ6R2U4WDJTVzlPdW1xRFZremExcFEwalFobmMvUlp0aDE4MDl0UFcvQUlVL2phUnZTYXJGWUx3T1l6UytaV1pzbmd3NWx1OXJGUXBheVVjUC94N1NydXNuWjZiZXJDMmFsTFYyY3VUbC9mc3RkNlhRdDM3dTV4eDdzN3B5bmUxVFhiWGZGTkhlTk9hT29XcHkxVEZkYVdvRkxKemdHL0xPbTd6SDJuV3JXVXorTTJVUUNQVW9XNXhoVHR4emlzN2U0ZDVDN0g1b1V0SFdmRElzRWRwUnQ4K3lQZThNZ2w4Z0h6ZmVHYytmRytSbW0yZjY1cDB5anp6dEd2SXl2NXhKbWxZME53bWFyQUpkcmNqOWJ5ZnU5TDhlZHcvVzlacHE3dEpENG1xa3o4eXRiMGdubFp5eElscHhrK0p0TFpuaExEWDYwQWFwYk5SUkZFQ2tZQVFRS01LbDNobXBaZkdvc3pYMFdDbXg4TkwzNXdhM2dYZ1FzTW42TEpSWlgrSmliT3NJSXV6ckFONGhSWDZRMlBSSWpwLy9zeVovdjYyTjdKcnlENWg1enRCRVRwUWgrZ2xPaHNjdUNaa3NGQjBpa0hOTmk1YklTZHN2RjJ3OHZpZ0JoVDRsaW8yK1Zqc2VPZEIyM1BudTFZdFAwM0xNSHgxNlFjNFdYREpodnAyR1U1dHpPTktMdm1kdTJ0OXFSc3o2VGRScnVldHEvUkJhU3NOcnFhbkxLZGxBNk1tdGxDZkxLT1JiWlJjWEM5ZkpnUEFvYnk4NzA4NVEveXU1bGJjaWMvZ0d0YmJBY0c0aXpoUSsvYk1TSEtjdUxhMXlDRWVvRUtmT3o3c1YyWS95RGZ4VGZTbmRRL0ZPTTdlRUdJZmtjNDFQOWQ0ZTNvMEdtMmN6L0M2K0dHdEc2Q2FnanZ1bTJvOXBzbVZEdGlRYlh3SnFqR3Yvc1ROMVJEOEFQd3c0OTdrSWlnQldyK3hTRGI3QjRpSHViZ0RCTnZ2YzFjWmdQWUVxbTNyN08xV3hPMlFIb0VZanZxTVhPbEZjRWNtR0tkQVB3YUcyQjUwZ2x2aVpDdUIxSFRWRnNNMXdUU3JYWFZ1eEhTTVhq'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
