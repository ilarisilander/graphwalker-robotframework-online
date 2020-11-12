
// function getModel() {
//   let file = document.querySelector('#file-input').files[0];
//   let reader = new FileReader();
//   reader.addEventListener('load', (e) => {
//     let text = e.target.result;
//     initiateModel(text);
//   });
//   reader.readAsText(file);
// };
//
// var cy = cytoscape({
//   container: document.getElementById('cy'),
//   style: [
//     {
//       selector: 'node',
//       style: {
//         'background-color': 'data(color)',
//         'padding-left': '5',
//         'padding-right': '5',
//         'padding-top': '5',
//         'padding-bottom': '5',
//         'shape': 'roundrectangle',
//         'label': 'data(name)',
//         'text-wrap': 'wrap',
//         'text-valign': 'center',
//         'text-halign': 'center',
//         'width': 'data(width)'
//       }
//     },
//     {
//       selector: 'edge',
//       style: {
//         'label': 'data(name)',
//         'width': 4,
//         'curve-style': 'bezier',
//         'line-color': 'data(color)',
//         'text-rotation': 'autorotate',
//         'target-arrow-shape': 'triangle',
//         'text-wrap': 'wrap'
//       }
//     }
//   ]
//
// })
//
// function initiateModel(json) {
//   // Make file into a json object
//   let jsonFile = JSON.parse(json);
//
//   for(var i = 0; i < jsonFile.models.length; i++) {
//     // Verticies
//     for(var key in jsonFile.models[i].vertices) {
//       if(jsonFile.models[i].vertices.hasOwnProperty(key)) {
//         cy.add({
//           group: 'nodes',
//           data: {
//             id: jsonFile.models[i].vertices[key].id,
//             name: jsonFile.models[i].vertices[key].name,
//             width: jsonFile.models[i].vertices[key].name.length * 10,
//             color: 'lightblue'
//           },
//           position: {
//             x: jsonFile.models[i].vertices[key].properties.x,
//             y: jsonFile.models[i].vertices[key].properties.y
//           }
//         })
//         //console.log(jsonFile.models[i].vertices[key].name);
//       }
//     }
//     // Edges
//     for(var key in jsonFile.models[i].edges) {
//       if(jsonFile.models[i].edges.hasOwnProperty(key)) {
//         cy.add({
//           group: 'edges',
//           data: {
//             id: jsonFile.models[i].edges[key].id,
//             name: jsonFile.models[i].edges[key].name,
//             source: jsonFile.models[i].edges[key].sourceVertexId,
//             target: jsonFile.models[i].edges[key].targetVertexId,
//             color: 'lightblue'
//           }
//         })
//         //console.log(jsonFile.models[i].edges[key]);
//       }
//     }
//   }
//   //console.log(cy.getElementById('j'));
// }
