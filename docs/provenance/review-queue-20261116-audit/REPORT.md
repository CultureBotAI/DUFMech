# DUFMech PR payload preservation audit

Captured main: `a030cca0dae2771e961ae12474c24c47a32b1363`. Audited 99/99 captured open PR heads.

Every changed path was compared against current published main and all other captured open PR heads. Exact containment requires the same Git object, mode and type (or proven absence for deletions). The comparison is based on the merge-base three-dot delta; branch age and titles are not evidence of supersession.

Closure candidates: none. No branch or review payload may be discarded on the basis of this audit.

| PR | Exact head | Three-dot paths | Head ancestors among other targets | Complete payload in | Disposition |
|---|---|---:|---|---|---|
| #280 | `7619bbd5376db6a9527fc767acb61a2a3f0b8bcf` | 13 | none | none | retain_unique_nonbatch_payload_manual_review_required |
| #289 | `8ddd241669fc18d7bd85609877933ad131b5ea1b` | 20 | none | none | retain_unique_immutable_review_payload |
| #290 | `5c2cf7732728db2632309e7952e413af3eb6e33d` | 20 | none | none | retain_unique_immutable_review_payload |
| #291 | `186d9c0cc0b701e8e2379c08e1a19ca4fc52437b` | 20 | none | none | retain_unique_immutable_review_payload |
| #292 | `7a1954593058eba3641e02dfdb92e996db291f53` | 20 | none | none | retain_unique_immutable_review_payload |
| #293 | `4e32604432414a92741e40b17322f5819cab6e87` | 20 | none | none | retain_unique_immutable_review_payload |
| #294 | `9f34cc5a5020ec88734217640276e67117b6e252` | 20 | none | none | retain_unique_immutable_review_payload |
| #295 | `4486602b0457b4b404d160b38f2b453a20d56fd2` | 20 | none | none | retain_unique_immutable_review_payload |
| #296 | `c9f21cb14426dd2258379b237de5c4e7dbfc6631` | 20 | none | none | retain_unique_immutable_review_payload |
| #297 | `788b2d9d53af495e794b9b061e597478d4cfebfe` | 20 | none | none | retain_unique_immutable_review_payload |
| #298 | `46f9432d78358afcfc3bbe90229a0fd968bee78f` | 20 | none | none | retain_unique_immutable_review_payload |
| #299 | `6ce737969ce716574346fc506e9736a55216e283` | 20 | none | none | retain_unique_immutable_review_payload |
| #300 | `24b98bf35cfbcb14e584798f418e9410595ddf27` | 20 | none | none | retain_unique_immutable_review_payload |
| #301 | `1ecc85fd9d2af418ff5f2cf05219d8fbd4e3f36b` | 20 | none | none | retain_unique_immutable_review_payload |
| #302 | `32ff45434dec44aeef319b152cd8e77db517a0ab` | 20 | none | none | retain_unique_immutable_review_payload |
| #303 | `1660edb749a0d0a4eb3f93a2727a0604110aeedb` | 20 | none | none | retain_unique_immutable_review_payload |
| #304 | `ffc3be86b1c8440bc351dd29f9722fd1612ad9b3` | 20 | none | none | retain_unique_immutable_review_payload |
| #305 | `36985881f1296bbf7855d097bae6ae374a025307` | 20 | none | none | retain_unique_immutable_review_payload |
| #306 | `e7c2021d554add517ce3a7affe1c58abd86cde77` | 20 | none | none | retain_unique_immutable_review_payload |
| #307 | `2370a0399b6bbb7f3227f7fc6d46cacaea68ce3e` | 20 | none | none | retain_unique_immutable_review_payload |
| #308 | `f15ac5afecd0ed18f78e86c59245d1aab045161e` | 20 | none | none | retain_unique_immutable_review_payload |
| #309 | `a1cd9d54b76271f94ca9bdb5a730e3e2c55f0a9c` | 20 | none | none | retain_unique_immutable_review_payload |
| #310 | `626b879040ed4b2cbd481e03b230d650e91b7a61` | 20 | none | none | retain_unique_immutable_review_payload |
| #311 | `20633a106dcff8a35701b197eadce9c8e6a67d89` | 20 | none | none | retain_unique_immutable_review_payload |
| #312 | `a08832ddf88923ee3c3e91f25c8ebad7719c108f` | 20 | none | none | retain_unique_immutable_review_payload |
| #313 | `7517d2795862472ca908d13a094f661a34a1de00` | 20 | none | none | retain_unique_immutable_review_payload |
| #314 | `bcde198e47db10b77b449ca543dc40a25c2f25dc` | 20 | none | none | retain_unique_immutable_review_payload |
| #315 | `7fb9cf3b9a32370884363c994138e7fe3d851ac0` | 20 | none | none | retain_unique_immutable_review_payload |
| #316 | `54279929d74f87c8eb39b3e555896a6afc907edb` | 20 | none | none | retain_unique_immutable_review_payload |
| #317 | `eaec3dd84837504527ec757ba73c04f6bcfc2064` | 20 | none | none | retain_unique_immutable_review_payload |
| #318 | `da3260f59504cfe7f6264e35de3d64fcea015aa2` | 20 | none | none | retain_unique_immutable_review_payload |
| #320 | `6f1d96da33e1fe777d000c759aaa90bd8f0c4800` | 20 | none | none | retain_unique_immutable_review_payload |
| #321 | `b1f759bfe3245a09129f84613df0b2885e8a7a34` | 20 | none | none | retain_unique_immutable_review_payload |
| #322 | `faef50e3c478ebd3da3513eda2fba0da7eda5848` | 20 | none | none | retain_unique_immutable_review_payload |
| #323 | `b62d303e33e365bdab4a4f518988ee81c9ce54d3` | 20 | none | none | retain_unique_immutable_review_payload |
| #324 | `4729f00be89239e94bd2ae8021982a1892b2215c` | 20 | none | none | retain_unique_immutable_review_payload |
| #325 | `75badeda99ad727ad8a2c3da92edfe659a2b5dd2` | 20 | none | none | retain_unique_immutable_review_payload |
| #326 | `3041be646f79caed2bb8d9cfc68765674366534c` | 20 | none | none | retain_unique_immutable_review_payload |
| #327 | `e90e23bfa3c4871b39ca987a83b25d766af98bfb` | 20 | none | none | retain_unique_immutable_review_payload |
| #328 | `80ea325a53ad887a265bffed11fe979f2f938c68` | 20 | none | none | retain_unique_immutable_review_payload |
| #329 | `4edcc2bf3b4fe0930ce8312ca811033412b4b8b9` | 20 | none | none | retain_unique_immutable_review_payload |
| #330 | `81610d27869d2dcdfb9afbce7eaba9862d5d7b07` | 20 | none | none | retain_unique_immutable_review_payload |
| #331 | `52a87dae4bfcbccb9a1c01556f001c1ac57d4453` | 20 | none | none | retain_unique_immutable_review_payload |
| #332 | `096c9a3d4e088b232f28e2664a2925c47f6b24cd` | 20 | none | none | retain_unique_immutable_review_payload |
| #368 | `c03590c8d68ed3082f5c2635aa4b7b7ab8c43440` | 8649 | none | none | retain_unique_nonbatch_payload_manual_review_required |
| #385 | `8048d2908d2d8f61154acb4448c2047c63991b64` | 10 | none | none | retain_unique_nonbatch_payload_manual_review_required |
| #403 | `d60ce421e93403b26b7103f3bbc0ec9326bf441e` | 20 | none | none | retain_unique_immutable_review_payload |
| #404 | `de04be095f9c4f72ad78bb6b15531fd9cc2d7d8b` | 20 | none | none | retain_unique_immutable_review_payload |
| #405 | `9982187d270f8bca59d9356742728bf56dc64ce1` | 20 | none | none | retain_unique_immutable_review_payload |
| #406 | `b88294ea68b9540432c727a9f22636915289345c` | 20 | none | none | retain_unique_immutable_review_payload |
| #407 | `d536c193dc39bb49da3b5965b848eb93d0e3282c` | 20 | none | none | retain_unique_immutable_review_payload |
| #408 | `f933c1c6113ccd36a72d0d4f90a181a0522e8ece` | 20 | none | none | retain_unique_immutable_review_payload |
| #409 | `a4616688c1355f75cfebc127921ce9de66c4b669` | 20 | none | none | retain_unique_immutable_review_payload |
| #410 | `1ae5a6875c4ce565c017df035c2ccf52b83df0fd` | 20 | none | none | retain_unique_immutable_review_payload |
| #411 | `93d690628f655fb4077da6c99e0f2e55ee274163` | 20 | none | none | retain_unique_immutable_review_payload |
| #412 | `cea84a65729b149dd0ad963003f5267518a3bdde` | 20 | none | none | retain_unique_immutable_review_payload |
| #413 | `f8cdee69cb2ae390e11c89f342928c26f6d0d46a` | 20 | none | none | retain_unique_immutable_review_payload |
| #414 | `467d9f5e71d57b07fd30af025fec5a9a25ba4bbc` | 20 | none | none | retain_unique_immutable_review_payload |
| #415 | `c2f6d94678c844612b337024c23a269b2b734a12` | 20 | none | none | retain_unique_immutable_review_payload |
| #416 | `058b8d60287f70ac338aa93c2b594356717906f5` | 20 | none | none | retain_unique_immutable_review_payload |
| #417 | `33d5df979414f823a9d2cc5f6634f7c30f3326e0` | 20 | none | none | retain_unique_immutable_review_payload |
| #418 | `5749df7520a97543fdb9c52a4aaa35bab40de50f` | 20 | none | none | retain_unique_immutable_review_payload |
| #419 | `a70c401ba0353405912bb73438bf3a3b142dac10` | 20 | none | none | retain_unique_immutable_review_payload |
| #420 | `13cd807489481ef3abdd5e8fb307d33611ce3359` | 20 | none | none | retain_unique_immutable_review_payload |
| #421 | `4f3395b8ff761cbf8302f2c25f2208a79cd01449` | 20 | none | none | retain_unique_immutable_review_payload |
| #422 | `698395d83ba29993475b24feeb92a60deafac77a` | 20 | none | none | retain_unique_immutable_review_payload |
| #423 | `9a6b6120eb6e834ba4ec73d7180aa35be7586374` | 20 | none | none | retain_unique_immutable_review_payload |
| #424 | `9cb92e094c6ae504b0164d75c5272ddd322995ee` | 20 | none | none | retain_unique_immutable_review_payload |
| #425 | `20249909bda89d32ce28d6f2c91854feefdb1bf9` | 20 | none | none | retain_unique_immutable_review_payload |
| #426 | `de6668d8aaeb80663bce36603d7615986d8cea15` | 20 | none | none | retain_unique_immutable_review_payload |
| #427 | `353141507e9d68e292bad2bd04490f6ce0878fe7` | 20 | none | none | retain_unique_immutable_review_payload |
| #428 | `578e4ee433c60c8f5b66514eaaaab3f1dda07adf` | 20 | none | none | retain_unique_immutable_review_payload |
| #429 | `0635c6ea9cac6b59e4a5b53dc9894b75b47cf59b` | 20 | none | none | retain_unique_immutable_review_payload |
| #430 | `cfb7d018a05dfd2a3f7a27c85c52415f9c0ff996` | 20 | none | none | retain_unique_immutable_review_payload |
| #431 | `37714327cdbd36031d6a5b53745a50cab4f07f2b` | 20 | none | none | retain_unique_immutable_review_payload |
| #432 | `a5ecc74276bb70d1ce16448bdf8954610c12edd5` | 20 | none | none | retain_unique_immutable_review_payload |
| #433 | `de27512e83ea7784aeae4450bfdf98b13b43f7b0` | 20 | none | none | retain_unique_immutable_review_payload |
| #434 | `d6bf872f0d06aaea984b6c2a75f0f6493ebb6ca3` | 20 | none | none | retain_unique_immutable_review_payload |
| #435 | `19848b5eed6505e53053cd634e5ed428d84669b4` | 20 | none | none | retain_unique_immutable_review_payload |
| #436 | `f70b44f22f7702528d4ed63b8360cd1d2c42b020` | 20 | none | none | retain_unique_immutable_review_payload |
| #437 | `03d76a3763c9f6d6004106c940cef024a7ac2743` | 20 | none | none | retain_unique_immutable_review_payload |
| #438 | `4c4283de85c871692a5fd9ac80300a83bdce5009` | 20 | none | none | retain_unique_immutable_review_payload |
| #439 | `a479b7bdf9d8e56d11c16f1fd872c6b985544e49` | 20 | none | none | retain_unique_immutable_review_payload |
| #440 | `dd3d1b5e67dc66d3f8085ba94eb25baf06d359bb` | 20 | none | none | retain_unique_immutable_review_payload |
| #441 | `3becaf611217d8da5e39c80c13100987098ff93e` | 20 | none | none | retain_unique_immutable_review_payload |
| #442 | `3f195acacdc541bcba626f221665321c2c0f8486` | 20 | none | none | retain_unique_immutable_review_payload |
| #443 | `99be47fa6d0b7150bfdcbbb03edea9c3bb5e2034` | 20 | none | none | retain_unique_immutable_review_payload |
| #444 | `2ad0c47264485325208fec32771d1398dba7780a` | 20 | none | none | retain_unique_immutable_review_payload |
| #445 | `c37386c0cdd4d3b71a79dc40ff8f8a2cf47bbc4b` | 20 | none | none | retain_unique_immutable_review_payload |
| #446 | `3557c3f42aac4c130333a7a157e6f37b3af5a653` | 20 | none | none | retain_unique_immutable_review_payload |
| #447 | `2fe9a660e0571192fdd89f78155c941a3b5b771e` | 20 | none | none | retain_unique_immutable_review_payload |
| #448 | `c91d962e9e4d8bd9f6dc208ff7d503e7444b3d56` | 20 | none | none | retain_unique_immutable_review_payload |
| #449 | `973b00d60e8a45a72943eaa93bb57ea61d7053a1` | 20 | none | none | retain_unique_immutable_review_payload |
| #450 | `0a5f0ddc9080b12a8e8decfebba88afb0d034c9e` | 20 | none | none | retain_unique_immutable_review_payload |
| #451 | `70f37d3f62334ddec9655ea9896d1c7e79b1a517` | 20 | none | none | retain_unique_immutable_review_payload |
| #452 | `3bf42be42f807b96480f3f288b549cc085e9b7de` | 20 | none | none | retain_unique_immutable_review_payload |
| #453 | `1a847c9181774e8df71d7b8579b72e748f36091f` | 20 | none | none | retain_unique_immutable_review_payload |
| #454 | `519e6312c45cb9eb7ce4555d0d2cc5f42a65c3fc` | 20 | none | none | retain_unique_immutable_review_payload |
| #457 | `0efc291a32e4ebeb1512c74f9f57a6b7884d7ee5` | 4 | none | none | retain_unique_nonbatch_payload_manual_review_required |

The complete JSON ledger records every path and its blob/mode/type, all compared commit/tree identities, ancestry, exact matches, and API/Git path coverage. This is a structural preservation audit, not an assessment of scientific validity or review quality. Live heads must be rechecked before acting.

Issue: not applicable to this read-only evidence helper. No source or Git/GitHub state was changed.
