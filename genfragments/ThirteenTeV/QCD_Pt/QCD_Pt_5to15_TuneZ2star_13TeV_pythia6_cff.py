import FWCore.ParameterSet.Config as cms

pythiaUESettingsBlock = cms.PSet(
        pythiaUESettings = cms.vstring(
                'MSTU(21)=1     ! Check on possible errors during program execution',
                'MSTJ(22)=2     ! Decay those unstable particles',
                'PARJ(71)=10 .  ! for which ctau  10 mm',
                'MSTP(33)=0     ! no K factors in hard cross sections',
                'MSTP(2)=1      ! which order running alphaS',
                'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)',
                'MSTP(52)=2     ! work with LHAPDF',

                'PARP(82)=1.921 ! pt cutoff for multiparton interactions',
                'PARP(89)=1800. ! sqrts for which PARP82 is set',
                'PARP(90)=0.227 ! Multiple interactions: rescaling power',

                'MSTP(95)=6     ! CR (color reconnection parameters)',
                'PARP(77)=1.016 ! CR',
                'PARP(78)=0.538 ! CR',

                'PARP(80)=0.1   ! Prob. colored parton from BBR',

                'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter',
                'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter',

                'PARP(62)=1.025 ! ISR cutoff',

                'MSTP(91)=1     ! Gaussian primordial kT',
                'PARP(93)=10.0  ! primordial kT-max',

                'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default',
                'MSTP(82)=4     ! Defines the multi-parton model',
        )
)

generator = cms.EDFilter('Pythia6GeneratorFilter',
	comEnergy = cms.double(13000.0),
	crossSection = cms.untracked.double(7.16e+10),
	filterEfficiency = cms.untracked.double(1),
	maxEventsToPrint = cms.untracked.int32(0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	pythiaPylistVerbosity = cms.untracked.int32(0),

	PythiaParameters = cms.PSet(
		pythiaUESettingsBlock,
		processParameters = cms.vstring(
			'MSEL = 1        ! QCD hight pT processes',
			'CKIN(3) = 5     ! minimum pt hat for hard interactions',
			'CKIN(4) = 15    ! maximum pt hat for hard interactions',
		),
		parameterSets = cms.vstring(
			'pythiaUESettings',
			'processParameters',
		)
	)
)

pthat_filter = cms.EDFilter('MCProcessFilter',
	MaxPthat = cms.untracked.vdouble(15., 15.0, 15.0, 15.0, 15.0, 15.0),
	ProcessID = cms.untracked.vint32(11, 12, 13, 68, 28, 53),
	MinPthat = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
)

ProductionFilterSequence = cms.Sequence(generator * pthat_filter)
