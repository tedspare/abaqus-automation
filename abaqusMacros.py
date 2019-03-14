# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Iterate():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.0, 0.0), point2=(220.0, 170.0))
    p = mdb.models['Model-1'].Part(name='Plate', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Plate']
    p.BaseSolidExtrude(sketch=s, depth=3.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Plate']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Plate']
    f, e = p.faces, p.edges
    p.HoleThruAllFromEdges(plane=f[4], edge1=e[10], edge2=e[0], planeSide=SIDE1, 
        diameter=10.0, distance1=20.0, distance2=20.0)
    p = mdb.models['Model-1'].parts['Plate']
    f1, e1 = p.faces, p.edges
    p.HoleThruAllFromEdges(plane=f1[5], edge1=e1[12], edge2=e1[9], planeSide=SIDE1, 
        diameter=10.0, distance1=20.0, distance2=20.0)
    p = mdb.models['Model-1'].parts['Plate']
    f, e = p.faces, p.edges
    p.HoleThruAllFromEdges(plane=f[6], edge1=e[4], edge2=e[8], planeSide=SIDE1, 
        diameter=10.0, distance1=20.0, distance2=40.0)
    p = mdb.models['Model-1'].parts['Plate']
    f1, e1 = p.faces, p.edges
    p.HoleThruAllFromEdges(plane=f1[7], edge1=e1[10], edge2=e1[6], planeSide=SIDE1, 
        diameter=10.0, distance1=50.0, distance2=100.0)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='Acrylic')
    mdb.models['Model-1'].materials['Acrylic'].Density(table=((1190.0, ), ))
    mdb.models['Model-1'].materials['Acrylic'].Elastic(table=((2800000000.0, 0.35), 
        ))
    mdb.models['Model-1'].materials['Acrylic'].Plastic(table=((69000000.0, 
        0.0), (70000000.0, 0.1)))
    mdb.models['Model-1'].HomogeneousSolidSection(name='Main', material='Acrylic', 
        thickness=None)
    p = mdb.models['Model-1'].parts['Plate']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(cells=cells)
    p = mdb.models['Model-1'].parts['Plate']
    p.SectionAssignment(region=region, sectionName='Main', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Plate']
    a.Instance(name='Plate-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].StaticStep(name='StepUno', previous='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='StepUno')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=407.02, 
        farPlane=761.712, width=377.87, height=164.953, viewOffsetX=76.5331, 
        viewOffsetY=-4.80688)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Plate-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#e ]', ), )
    region = a.Set(faces=faces1, name='StaticPins')
    mdb.models['Model-1'].DisplacementBC(name='PinsABC', createStepName='StepUno', 
        region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=456.918, 
        farPlane=711.813, width=79.7747, height=34.8243, viewOffsetX=5.43008, 
        viewOffsetY=20.0979)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Plate-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(faces=faces1)
    mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='StepUno', 
        region=region, u1=UNSET, u2=7.0, u3=UNSET, ur1=UNSET, ur2=UNSET, 
        ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
        fieldName='', localCsys=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=415.691, 
        farPlane=753.04, width=315.285, height=137.632, viewOffsetX=3.99397, 
        viewOffsetY=-7.50845)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p1 = mdb.models['Model-1'].parts['Plate']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Model-1'].parts['Plate']
    p.seedPart(size=20.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Plate']
    p.generateMesh()
    a1 = mdb.models['Model-1'].rootAssembly
    a1.regenerate()
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    mdb.Job(name='SendIt', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB)
    mdb.jobs['SendIt'].submit(consistencyChecking=OFF)
    mdb.jobs['SendIt'].writeInput(consistencyChecking=OFF)
    session.mdbData.summary()
    o3 = session.openOdb(name='C:/ABAQUS2/IterativeDesign/SendIt.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.printToFile(
        fileName='C:/ABAQUS2/IterativeDesign/MECH321_DesignProject_Iterative', 
        format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=409.205, 
        farPlane=740.761, width=387.177, height=169.016, cameraPosition=(
        -74.2658, 420.327, 432.784), cameraUpVector=(0.32944, 0.57735, 
        -0.747085), cameraTarget=(118.248, 82.9435, -3.78665))
    session.printToFile(
        fileName='C:/ABAQUS2/IterativeDesign/MECH321_DesignProject_Iterative_2', 
        format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))


def JustJobs():
    
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior

    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    mdb.jobs['Modified'].submit(consistencyChecking=OFF)
    session.mdbData.summary()
    session.viewports['Viewport: 1'].setValues(
        displayedObject=session.odbs['C:/ABAQUS2/Jobs/Modified.odb'])
    o3 = session.openOdb(name='C:/ABAQUS2/IterativeDesign/Modified.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.printToFile(
        fileName='C:/ABAQUS2/IterativeDesign/MECH321_DesignProject_Iterative_5.png', 
        format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=381.67, 
        farPlane=765.741, width=361.124, height=157.643, cameraPosition=(
        -217.639, 420.327, 334.994), cameraUpVector=(0.575304, 0.57735, 
        -0.579389), cameraTarget=(118.549, 82.9435, -3.58089))
    session.printToFile(
        fileName='C:/ABAQUS2/IterativeDesign/MECH321_DesignProject_Iterative_6.png', 
        format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))


def ProbeValues():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
