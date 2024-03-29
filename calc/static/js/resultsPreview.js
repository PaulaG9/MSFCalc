function netPatients(numpatients, duration, monincrease){
    if(duration/30>1){
        final_mth_patients=numpatients+(Math.round(duration/30)-1)*monincrease
        net_patients=((numpatients+final_mth_patients)*Math.round(duration/30))/2
    } else{
        net_patients=numpatients+monincrease 
    }
    return net_patients;
}

function estResults(net_patients, duration, frequency, units, packaging, packaging_size){
    if(packaging=='bottle'){
        est_results=(net_patients * duration * frequency * units* 5)/packaging_size;
        if(est_results){
            return (est_results+ ' bottles');
        }        
    }else{
        est_results=net_patients * duration * frequency * units;
        if(est_results){
            return ( est_results+ ' ' + packaging + 's');
        }        
    }    
}

function getPreview(){
    
    var formInst=$('input[id^=duration_]')
    
    for (var x=1; x<formInst.length+1; x++){
        
        var duration=parseInt($('input#duration_' +x).val())*30; 
        console.log(duration);
        var monincrease=parseInt($('input#monthly_increase_' +x).val()); 
        console.log(monincrease);
        var results=$('[id^=result_'+ x +']')
        for (var i=1; i<results.length+1; i++){ 
            console.log(i-1, results.eq(i-1))           
            var txt=results.eq(i-1).attr("id")
            var msfcode=txt.split("_")[2]            
            var frequency=parseInt($('select#frequency_'+ x +'_' + msfcode).val()); 
            console.log(frequency);
            var numpatients=parseFloat($('input#num_patients_' + x +'_' + msfcode).val()); 
            console.log(numpatients);   
            var units=parseFloat($('input#unit_per_patient_'+ x + '_' + msfcode).val());
            console.log(units)
            var packaging=$('p#package_' + x + '_' + msfcode).text().split(' ')[2];
            console.log(packaging)
            var packaging_size=$('p#package_' + x + '_' + msfcode).text().split(' ')[0]
            console.log(packaging_size)

            estimate=estResults(netPatients(numpatients, duration, monincrease),duration, frequency, units, packaging, packaging_size);                 
            console.log(estimate);

            results.eq(i-1).text(estimate);
        }
    }       
}

function putPatients(){
    var formInst2=$('input[id^=patients_in_cohort]')
    for (var z=1; z<formInst2.length+1; z++){
        var patientsCohort=parseInt($('input#patients_in_cohort_' +z).val());
        console.log(patientsCohort);
        var patientsNum=$('[id^=num_patients_' + z+']');
        for (var t=1; t<patientsNum.length+1; t++){
            var txt=patientsNum.eq(t-1).attr("id");
            var msfcode=txt.split("_")[3];
            console.log(txt,msfcode)
            var ratio=parseFloat($('p#patients_percentage_'+ z +'_'+msfcode).text());
            console.log(ratio)
            calculatedPatients=(ratio * patientsCohort)/100;
            console.log(calculatedPatients )
            patientsNum.eq(t-1).val(calculatedPatients);
        }
    }
}

